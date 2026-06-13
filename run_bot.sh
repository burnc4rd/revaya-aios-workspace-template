#!/bin/bash

# Navigate to the workspace root
cd "$(dirname "$0")"

# Verify .env file exists
if [ ! -f .env ]; then
    echo "❌ Error: .env file not found!"
    echo "Please copy .env.example to .env first:"
    echo "  cp .env.example .env"
    exit 1
fi

# Perform configuration checks
ERRORS=0

# Check for token placeholders
if grep -q "your-telegram-bot-token-here" .env || ! grep -q "TELEGRAM_BOT_TOKEN=" .env; then
    echo "❌ Configuration Error: TELEGRAM_BOT_TOKEN is missing or is set to a placeholder in .env."
    ERRORS=$((ERRORS + 1))
fi

if grep -q "your-gemini-api-key-here" .env || ! grep -q "GEMINI_API_KEY=" .env; then
    echo "❌ Configuration Error: GEMINI_API_KEY is missing or is set to a placeholder in .env."
    ERRORS=$((ERRORS + 1))
fi

if [ $ERRORS -gt 0 ]; then
    echo "Please open your .env file and configure your real credentials before running the bot."
    exit 1
fi

# Start the bot
echo "🚀 Starting CommandOS Telegram Bot via virtualenv..."
exec .venv/bin/python apps/command/main.py
