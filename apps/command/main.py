import asyncio
import logging
import sys
from pathlib import Path

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from apps.command import config, bot

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stdout
)
logger = logging.getLogger("CommandOS.Main")

async def main():
    logger.info("Initializing CommandOS Telegram Bot...")
    
    if not config.TELEGRAM_BOT_TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN environment variable not set! Exiting.")
        sys.exit(1)
        
    if not config.GEMINI_API_KEY:
        logger.error("GEMINI_API_KEY environment variable not set! Exiting.")
        sys.exit(1)
        
    if config.TELEGRAM_GROUP_ID == 0:
        logger.warning(
            "Bot is starting in DISCOVERY MODE (TELEGRAM_GROUP_ID is set to 0 or unconfigured). "
            "Send any message to the bot from your Telegram group to get your Group Chat ID."
        )
    else:
        logger.info(f"Bot authorized for Chat ID: {config.TELEGRAM_GROUP_ID}")
        
    try:
        # Start polling loop
        logger.info("CommandOS Bot is now polling for messages. Press Ctrl+C to stop.")
        await bot.dp.start_polling(bot.bot)
    except Exception as e:
        logger.critical(f"Bot execution halted due to critical error: {e}")
    finally:
        # Graceful shutdown
        await bot.bot.session.close()
        logger.info("CommandOS Bot session closed.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("CommandOS Bot stopped by user (Ctrl+C).")
        sys.exit(0)
