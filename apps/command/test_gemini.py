import logging
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from apps.command import config, agent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("CommandOS.Test")

def run_test():
    logger.info("Starting CommandOS local test...")
    
    # 1. Check Configuration
    logger.info(f"Workspace root: {config.WORKSPACE_ROOT}")
    if not config.GEMINI_API_KEY:
        logger.error("GEMINI_API_KEY is missing from environment. Cannot test.")
        return
        
    logger.info(f"Gemini API model configured: {config.COMMAND_GENERAL_MODEL}")
    
    # 2. Test Workspace File Reading
    logger.info("Reading CLAUDE.md...")
    claude_content = agent.read_file_content(config.WORKSPACE_ROOT / "CLAUDE.md")
    if not claude_content:
        logger.error("Failed to read CLAUDE.md. Check file permissions.")
        return
    logger.info(f"Successfully read CLAUDE.md ({len(claude_content)} characters).")
    
    # 3. Test Command Execution
    logger.info("Simulating execution of '/prime' command using Gemini...")
    try:
        reply_text, file_writes, moments = agent.execute_gemini_command("prime", "")
        
        print("\n" + "="*50)
        print("GEMINI REPLY TEXT:")
        print("="*50)
        print(reply_text)
        print("="*50 + "\n")
        
        print(f"Files written request: {file_writes}")
        print(f"Captured moments request: {moments}")
        logger.info("Test execute completed successfully!")
        
    except Exception as e:
        logger.error(f"Test failed with error: {e}", exc_info=True)

if __name__ == "__main__":
    run_test()
