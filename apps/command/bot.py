import logging
import io
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, ContentType
from aiogram.utils.markdown import hcode

from apps.command import config, agent

logger = logging.getLogger("CommandOS.Bot")

# Initialize aiogram elements
bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()
router = Router()

# Security Middleware/Filter to lock down chat ID
def is_authorized_chat(message: Message) -> bool:
    """Checks if the incoming message is from the authorized Telegram Group."""
    if config.TELEGRAM_GROUP_ID == 0:
        # Discovery Mode — allow all chats temporarily to help user find group ID
        return True
    return message.chat.id == config.TELEGRAM_GROUP_ID


@router.message(F.chat.id != config.TELEGRAM_GROUP_ID)
async def handle_unauthorized(message: Message):
    """Handles unauthorized messages or discovery mode logging."""
    if config.TELEGRAM_GROUP_ID == 0:
        logger.info(f"CommandOS Discovery Mode: Received message in chat. Chat ID is: {message.chat.id}")
        await message.reply(
            f"👋 Welcome to CommandOS!\n\n"
            f"Your Telegram Chat ID is: {hcode(str(message.chat.id))}\n\n"
            f"To authorize this chat, please copy this ID and set it as "
            f"your {hcode('TELEGRAM_GROUP_ID')} in your workspace {hcode('.env')} file, then reboot the bot.",
            parse_mode="HTML"
        )
    else:
        logger.warning(f"Ignored unauthorized message from Chat ID {message.chat.id} (username: @{message.from_user.username})")


def process_command_results(reply_text: str, file_writes: dict, captured_moments: list) -> str:
    """Applies file writes and captures build moments to SQLite, appending status to the reply."""
    extra_replies = []
    
    # 1. Apply file writes to local system
    if file_writes:
        written = agent.execute_file_writes(file_writes)
        if written:
            extra_replies.append(f"📁 Files written: {', '.join(written)}")
            
    # 2. Apply build moments to database
    if captured_moments:
        try:
            from scripts.content.db import get_connection
            from scripts.content.writer import write_content_idea
            from scripts.content.generate_pipeline import main as generate_pipeline_main
            
            conn = get_connection()
            for moment in captured_moments:
                idea_id = write_content_idea(conn, moment)
                extra_replies.append(f"💡 Build moment captured as stub #{idea_id}: '{moment.get('title')}'")
            conn.close()
            
            # Regenerate the pipeline markdown file
            generate_pipeline_main()
        except Exception as e:
            logger.error(f"Failed to save build moment to database: {e}")
            extra_replies.append(f"⚠️ Error saving build moment to database: {e}")

    if extra_replies:
        return f"{reply_text}\n\n---\n" + "\n".join(extra_replies)
    return reply_text


async def send_response_in_chunks(message: Message, text: str, **kwargs):
    """Sends long text responses in chunks of 4000 characters to prevent Telegram API errors."""
    chunk_size = 4000
    if len(text) <= chunk_size:
        await message.reply(text, **kwargs)
        return
        
    chunks = []
    current_chunk = []
    current_length = 0
    
    for line in text.splitlines(keepends=True):
        if current_length + len(line) > chunk_size:
            if current_chunk:
                chunks.append("".join(current_chunk))
            current_chunk = [line]
            current_length = len(line)
        else:
            current_chunk.append(line)
            current_length += len(line)
            
    if current_chunk:
        chunks.append("".join(current_chunk))
        
    # Send chunks sequentially
    first = True
    for chunk in chunks:
        if not chunk.strip():
            continue
        if first:
            await message.reply(chunk, **kwargs)
            first = False
        else:
            await message.answer(chunk, **kwargs)


# --- Command Handlers ---

@router.message(Command("prime"))
async def handle_prime(message: Message, command: CommandObject):
    if not is_authorized_chat(message):
        return
    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")
    reply, files, moments = agent.execute_gemini_command("prime", command.args or "")
    final_reply = process_command_results(reply, files, moments)
    await send_response_in_chunks(message, final_reply)


@router.message(Command("build_guide", "build-guide"))
async def handle_build_guide(message: Message, command: CommandObject):
    if not is_authorized_chat(message):
        return
    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")
    reply, files, moments = agent.execute_gemini_command("build-guide", command.args or "")
    final_reply = process_command_results(reply, files, moments)
    await send_response_in_chunks(message, final_reply)


@router.message(Command("team"))
async def handle_team(message: Message, command: CommandObject):
    if not is_authorized_chat(message):
        return
    
    args = command.args
    if not args:
        await message.reply("Please specify a request for the team, e.g., `/team help me draft a post about my bottleneck`")
        return
        
    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")
    reply, files, moments = agent.execute_gemini_command("team", args)
    final_reply = process_command_results(reply, files, moments)
    await send_response_in_chunks(message, final_reply)


@router.message(Command("reflect"))
async def handle_reflect(message: Message, command: CommandObject):
    if not is_authorized_chat(message):
        return
        
    args = command.args
    if not args:
        await message.reply(
            "Please provide your reflection thoughts after the command, e.g.:\n"
            "`/reflect today I set up the Telegram bot. Aligned with bottleneck. No moments.`"
        )
        return
        
    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")
    reply, files, moments = agent.execute_gemini_command("reflect", args)
    final_reply = process_command_results(reply, files, moments)
    await send_response_in_chunks(message, final_reply)


@router.message(Command("capture"))
async def handle_capture(message: Message, command: CommandObject):
    if not is_authorized_chat(message):
        return
        
    args = command.args
    if not args:
        await message.reply("Please specify a task to capture: `/capture [task text]`")
        return
        
    try:
        from scripts.content.db import get_connection
        from scripts.content.writer import write_content_idea
        
        idea = {
            'title': args,
            'description': 'Quick captured task from Telegram',
            'channel': 'inbox',
            'source_type': 'quick_capture',
            'production_status': 'stub',
        }
        
        conn = get_connection()
        idea_id = write_content_idea(conn, idea)
        conn.close()
        
        await message.reply(f"📥 Captured to inbox as stub #{idea_id}")
    except Exception as e:
        logger.error(f"Failed to execute quick capture: {e}")
        await message.reply(f"⚠️ Error capturing task: {e}")


# --- Voice Note / Audio Handler ---

@router.message(F.voice)
async def handle_voice_note(message: Message):
    if not is_authorized_chat(message):
        return
        
    await message.bot.send_chat_action(chat_id=message.chat.id, action="record_voice")
    
    # Download the voice note file
    voice = message.voice
    file_info = await bot.get_file(voice.file_id)
    
    file_bytes = io.BytesIO()
    await bot.download_file(file_info.file_path, file_bytes)
    audio_data = file_bytes.getvalue()
    
    # Transcribe using Gemini's native audio understanding
    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")
    transcribed_text = agent.transcribe_audio_bytes(audio_data, mime_type="audio/ogg")
    
    logger.info(f"Transcribed voice note: '{transcribed_text}'")
    
    # Determine if it's a command or general chat
    if transcribed_text.startswith("/") or transcribed_text.lower().startswith("run /"):
        # Normalize spoken command (e.g. "run /build-guide" -> "/build_guide")
        cmd_text = transcribed_text.lower().replace("run ", "").strip()
        parts = cmd_text.split(" ", 1)
        cmd_name = parts[0].replace("/", "")
        args = parts[1] if len(parts) > 1 else ""
        
        # Route to appropriate command
        await message.reply(f"🎙️ *Heard command:* `/{cmd_name} {args}`\n_Processing..._")
        reply, files, moments = agent.execute_gemini_command(cmd_name, args)
        final_reply = process_command_results(reply, files, moments)
        await send_response_in_chunks(message, final_reply)
    else:
        # Fallback to general workspace assistant
        await message.reply(f"🎙️ *Heard:* \"{transcribed_text}\"\n_Generating response..._")
        reply = agent.query_general_agent(transcribed_text)
        await send_response_in_chunks(message, reply)


# --- General Text Handler ---

@router.message(F.text)
async def handle_text_message(message: Message):
    if not is_authorized_chat(message):
        return
        
    # Ignore slash commands (they are handled by Command filter)
    if message.text.startswith("/"):
        # Unknown slash command
        await message.reply(f"❓ Unknown command. Available commands: `/prime`, `/build_guide`, `/team`, `/reflect`, `/capture`")
        return
        
    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")
    # Route general message to Chief of Staff agent
    reply = agent.query_general_agent(message.text)
    await send_response_in_chunks(message, reply)


# Register all routers
dp.include_router(router)
