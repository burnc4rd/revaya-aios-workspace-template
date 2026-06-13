import os
import re
import glob
import logging
from pathlib import Path
from datetime import datetime, timezone
import google.generativeai as genai
from apps.command import config

logger = logging.getLogger("CommandOS.Agent")

# Configure Gemini API
if config.GEMINI_API_KEY:
    genai.configure(api_key=config.GEMINI_API_KEY)
else:
    logger.error("Gemini API key is not configured. Direct calls to Gemini will fail.")


def read_file_content(path: Path) -> str:
    """Safely read file content as UTF-8. If path is a directory, read all files inside it."""
    if not path.exists():
        return ""
    if path.is_dir():
        contents = []
        for child in sorted(path.iterdir()):
            if child.is_file() and not child.name.startswith("."):
                file_content = read_file_content(child)
                contents.append(f"=== File: {child.name} ===\n{file_content}")
        return "\n\n".join(contents)
    try:
        return path.read_text(encoding="utf-8")
    except Exception as e:
        logger.error(f"Error reading file {path}: {e}")
        return ""


def get_obsidian_journals() -> str:
    """Reads all markdown files in the configured Obsidian vault under Build Journals."""
    if not config.OBSIDIAN_VAULT_PATH:
        return "Obsidian vault path not configured."
    
    journal_dir = config.OBSIDIAN_VAULT_PATH / "Build Journals"
    if not journal_dir.exists():
        return f"Journal directory not found at: {journal_dir}"
    
    journal_files = glob.glob(str(journal_dir / "*.md"))
    if not journal_files:
        return "No build journals found in the Obsidian vault."
    
    combined_content = []
    # Sort files to read recent ones or combine all (assuming they are small)
    for file_path in sorted(journal_files):
        p = Path(file_path)
        content = read_file_content(p)
        combined_content.append(f"--- Journal: {p.name} ---\n{content}\n")
        
    return "\n".join(combined_content)


def load_command_instructions(command_name: str) -> tuple[str, list[str]]:
    """Loads the command instructions file from .claude/commands/."""
    command_file = config.WORKSPACE_ROOT / ".claude" / "commands" / f"{command_name}.md"
    if not command_file.exists():
        raise FileNotFoundError(f"Command definition not found: {command_file}")
    
    content = read_file_content(command_file)
    
    # Parse the files listed under ## Read
    # Looks for lines after ## Read (until the next section ##) that name files
    read_section_match = re.search(r"## Read\s*\n(.*?)(?:\n##|$)", content, re.DOTALL)
    files_to_read = []
    if read_section_match:
        for line in read_section_match.group(1).splitlines():
            line = line.strip()
            # Clean up line formatting (numbers, lists, backticks)
            line = re.sub(r"^\d+\.\s*", "", line)  # e.g., "1. "
            line = re.sub(r"^-\s*", "", line)     # e.g., "- "
            line = line.strip("`'\" ")
            if line and not line.startswith("#") and "OBSIDIAN_VAULT_PATH" not in line:
                files_to_read.append(line)
                
    return content, files_to_read


def execute_gemini_command(command_name: str, user_input: str = "") -> tuple[str, dict[str, str]]:
    """Executes a command by loading its instructions, gathering required workspace files,

    calling the Gemini API, and parsing any file writes requested in the output.
    """
    try:
        # 1. Load instructions and get list of files to read
        instructions, files_to_read = load_command_instructions(command_name)
    except FileNotFoundError as e:
        return str(e), {}

    # 2. Gather Workspace Context
    workspace_context = []
    
    # Load default files (CLAUDE.md & oobg.md are always loaded as core context)
    claude_md = read_file_content(config.WORKSPACE_ROOT / "CLAUDE.md")
    oobg_md = read_file_content(config.WORKSPACE_ROOT / "strategic-layer" / "oobg.md")
    
    workspace_context.append(f"=== CLAUDE.md ===\n{claude_md}")
    workspace_context.append(f"=== strategic-layer/oobg.md ===\n{oobg_md}")
    
    # Load command-specific files
    for rel_path in files_to_read:
        file_path = config.WORKSPACE_ROOT / rel_path
        if file_path.exists():
            content = read_file_content(file_path)
            workspace_context.append(f"=== {rel_path} ===\n{content}")
            
    # Specialized Context: Obsidian Journals for build-guide
    if command_name == "build-guide" and config.OBSIDIAN_VAULT_PATH:
        journals_content = get_obsidian_journals()
        workspace_context.append(f"=== Obsidian Build Journals ===\n{journals_content}")

    context_str = "\n\n".join(workspace_context)
    
    # 3. Create System Prompt
    system_prompt = (
        "You are the Gemini Executor for the Business AI OS workspace.\n"
        "Your task is to run the workspace command specified below, adhering strictly to its rules, scoring, and output format.\n\n"
        "--- SYSTEM/WORKSPACE FILES CONTROLLING STATE ---\n"
        f"{context_str}\n\n"
        "--- COMMAND INSTRUCTIONS ---\n"
        f"{instructions}\n\n"
        "--- FILE WRITE CAPABILITY ---\n"
        "If you need to write or update a file as part of this command's execution (e.g., creating a reflect entry, updating GTD files, or writing a plan), "
        "you MUST include the file content inside your response using the following format:\n"
        "<<<WRITE_FILE:relative/path/to/file.md>>>\n"
        "File contents...\n"
        "<<<END_WRITE_FILE>>>\n"
        "The relative path must be relative to the workspace root. You can write multiple files in one response if needed.\n"
        "Any text outside of the <<<WRITE_FILE>>> blocks will be delivered directly to the user in Telegram."
    )

    # 4. Call Gemini
    try:
        model = genai.GenerativeModel(config.COMMAND_GENERAL_MODEL)
        prompt = f"Executing Command: /{command_name}\nUser input/arguments: {user_input}"
        
        logger.info(f"Calling Gemini ({config.COMMAND_GENERAL_MODEL}) for command /{command_name}...")
        response = model.generate_content(
            contents=[system_prompt, prompt],
            generation_config={"temperature": 0.2} # Keep temperature low for structured outputs
        )
        
        reply_text = response.text
    except Exception as e:
        logger.error(f"Gemini API call failed: {e}")
        return f"Error executing Gemini API: {e}", {}

    # 5. Parse and extract file writes and build moments
    file_writes = {}
    captured_moments = []
    
    # Find all WRITE_FILE blocks
    write_pattern = r"<<<WRITE_FILE:(.*?)>>>\n(.*?)<<<END_WRITE_FILE>>>"
    write_matches = re.findall(write_pattern, reply_text, re.DOTALL)
    
    for rel_path, file_content in write_matches:
        rel_path = rel_path.strip()
        file_writes[rel_path] = file_content.strip()
        
    # Find all CAPTURE_MOMENT blocks
    moment_pattern = r"<<<CAPTURE_MOMENT>>>\n(.*?)<<<END_CAPTURE_MOMENT>>>"
    moment_matches = re.findall(moment_pattern, reply_text, re.DOTALL)
    
    for json_str in moment_matches:
        try:
            import json
            idea = json.loads(json_str.strip())
            captured_moments.append(idea)
        except Exception as err:
            logger.error(f"Failed to parse captured moment JSON: {err}")
            
    # Clean up the response text so the tags aren't sent to the user
    clean_reply_text = re.sub(write_pattern, "", reply_text, flags=re.DOTALL)
    clean_reply_text = re.sub(moment_pattern, "", clean_reply_text, flags=re.DOTALL).strip()
    
    # If clean reply text is empty but files were written, confirm the write
    if not clean_reply_text and file_writes:
        written_files_str = ", ".join(file_writes.keys())
        clean_reply_text = f"✅ Successfully updated: {written_files_str}"

    return clean_reply_text, file_writes, captured_moments


def execute_file_writes(file_writes: dict[str, str]) -> list[str]:
    """Saves the requested file writes to the local file system."""
    written_paths = []
    for rel_path, content in file_writes.items():
        # Prevent directory traversal attacks
        if ".." in rel_path or rel_path.startswith("/"):
            logger.warning(f"Blocked suspicious file path write: {rel_path}")
            continue
            
        full_path = config.WORKSPACE_ROOT / rel_path
        try:
            # Ensure parent directories exist
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text(content, encoding="utf-8")
            written_paths.append(rel_path)
            logger.info(f"Wrote file to workspace: {rel_path}")
        except Exception as e:
            logger.error(f"Failed to write file {rel_path}: {e}")
            
    return written_paths


def query_general_agent(user_message: str, history: list = None) -> str:
    """Interacts with Gemini as a general workspace assistant/Chief of Staff,

    loading workspace context files as part of its system instructions.
    """
    claude_md = read_file_content(config.WORKSPACE_ROOT / "CLAUDE.md")
    oobg_md = read_file_content(config.WORKSPACE_ROOT / "strategic-layer" / "oobg.md")
    
    # Load context files
    context_files = ["personal-info.md", "business-info.md", "strategy.md", "current-data.md"]
    context_str = ""
    for f in context_files:
        content = read_file_content(config.WORKSPACE_ROOT / "context" / f)
        context_str += f"\n=== context/{f} ===\n{content}\n"
        
    system_prompt = (
        "You are the Chief of Staff agent for the Business AI OS workspace.\n"
        "Help the user navigate and operate their business using this workspace.\n"
        "You have full context about the business, owner, and current goals:\n\n"
        f"=== CLAUDE.md ===\n{claude_md}\n\n"
        f"=== strategic-layer/oobg.md ===\n{oobg_md}\n\n"
        f"{context_str}\n\n"
        "Provide concise, professional, and actionable support. Frame advice around their current OOBG Bottleneck."
    )
    
    try:
        model = genai.GenerativeModel(config.COMMAND_GENERAL_MODEL)
        response = model.generate_content(
            contents=[system_prompt, user_message]
        )
        return response.text
    except Exception as e:
        logger.error(f"General agent query failed: {e}")
        return f"Error querying Gemini: {e}"


def transcribe_audio_bytes(audio_bytes: bytes, mime_type: str = "audio/ogg") -> str:
    """Directly sends raw audio bytes to Gemini to transcribe it."""
    try:
        model = genai.GenerativeModel(config.COMMAND_GENERAL_MODEL)
        prompt = "Listen to this audio note. Transcribe the spoken text exactly. Do not add any extra commentary."
        
        response = model.generate_content([
            {
                "mime_type": mime_type,
                "data": audio_bytes
            },
            prompt
        ])
        return response.text.strip()
    except Exception as e:
        logger.error(f"Audio transcription failed: {e}")
        return f"[Error transcribing audio: {e}]"
