import os
from pathlib import Path
import logging
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("CommandOS.Config")

# Load environment variables
workspace_root = Path(__file__).resolve().parent.parent.parent
env_path = workspace_root / ".env"

if env_path.exists():
    load_dotenv(dotenv_path=env_path)
    logger.info(f"Loaded environment variables from: {env_path}")
else:
    load_dotenv()
    logger.warning(".env file not found in workspace root, falling back to system environment variables.")

# Required Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Check for required configuration
if not GEMINI_API_KEY:
    logger.error("GEMINI_API_KEY is missing! Please configure it in your .env file.")

if not TELEGRAM_BOT_TOKEN:
    logger.error("TELEGRAM_BOT_TOKEN is missing! Please configure it in your .env file.")

# Optional Keys
# Set TELEGRAM_GROUP_ID to 0 or leave empty for "Discovery Mode" (logs chat IDs of incoming messages)
group_id_str = os.getenv("TELEGRAM_GROUP_ID", "0")
try:
    TELEGRAM_GROUP_ID = int(group_id_str)
except ValueError:
    logger.warning(f"Invalid TELEGRAM_GROUP_ID: '{group_id_str}'. Defaulting to 0 (Discovery Mode).")
    TELEGRAM_GROUP_ID = 0

OBSIDIAN_VAULT_PATH = os.getenv("OBSIDIAN_VAULT_PATH")
if OBSIDIAN_VAULT_PATH:
    OBSIDIAN_VAULT_PATH = Path(OBSIDIAN_VAULT_PATH)
    if not OBSIDIAN_VAULT_PATH.exists():
         logger.warning(f"OBSIDIAN_VAULT_PATH '{OBSIDIAN_VAULT_PATH}' does not exist on disk!")
else:
    logger.warning("OBSIDIAN_VAULT_PATH is not configured. Features reading build journals will be disabled.")

# Bot tuning defaults
COMMAND_GENERAL_MODEL = os.getenv("COMMAND_GENERAL_MODEL", "gemini-2.5-flash")
WORKSPACE_ROOT = workspace_root
