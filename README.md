
# Web3 Twitter Post Bot 🤖

This is a Telegram bot that generates influencer-style tweets with images for 13 popular Web3 projects.

## ✅ Supported Commands
- `/post project_name` — Generate a tweet for a specific project
- `/random` — Random post from any project
- `/list_projects` — Shows all available project names
- `/help` — Shows usage instructions

## 🚀 Deploy to Railway

1. Clone this repo or upload it to GitHub
2. Create a Railway project
3. Add environment variable:
   - `API_TOKEN` — your Telegram bot token
4. Add a Procfile:
   ```
   worker: python bot.py
   ```
5. Done!

## 🧱 Built with
- Python 3.11+
- aiogram 3.7+
