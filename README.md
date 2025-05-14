# Web3 Twitter Post Bot 🤖

A Telegram bot that generates influencer-style tweets with images for Web3 projects.

## ✅ Supported Commands
- `/post project_name` — Generate a tweet for a specific project
- `/random` — Random post from any project
- `/list_projects` — See all supported projects
- `/help` — Show usage instructions

## 🚀 How to Deploy
1. Upload this project to Railway or any cloud.
2. Add environment variable: `API_TOKEN`
3. Railway will use `Procfile` to run the bot: `worker: python bot.py`

## 🧱 Built with
- Python 3.11+
- aiogram 3.7+
