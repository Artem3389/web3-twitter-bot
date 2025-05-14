
import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart, Command

# 🔐 Встав свій токен тут
API_TOKEN = "7670472776:AAFKugaQ4aBEM3lN9ioQJbRrIT3JI6zaM"

if not API_TOKEN or "REPLACE" in API_TOKEN:
    raise ValueError("❗ Please insert your actual Telegram API_TOKEN in the code")

projects_data = {
    'linera': [
        {'text': 'Linera is redefining blockchain scalability with parallel chains. The future of fast, secure infra is here. 🚀 #Linera #Web3 #Airdrop', 'image': 'https://cryptologos.cc/logos/linera-logo.png'},
        {'text': 'Scalable, fast, and async — Linera is the game-changer you’ve been waiting for. Don’t miss the ride. 🔥 #Layer1 #Linera', 'image': 'https://cryptologos.cc/logos/linera-banner.jpg'}
    ],
}

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

@dp.message(CommandStart())
async def start(message: Message):
    print(f"🔔 Received /start from {message.from_user.username}")
    await message.answer("Welcome! Use /post [project_name] to get a Web3 tweet. Use /help to see all commands.")

@dp.message(Command("help"))
async def help_handler(message: Message):
    print(f"🔔 Received /help from {message.from_user.username}")
    await message.answer("""Available commands:
/post [project_name] — get a tweet post for a project
/random — get a random project post
/list_projects — see all available project names""")

@dp.message(Command("list_projects"))
async def list_projects(message: Message):
    print(f"🔔 Received /list_projects from {message.from_user.username}")
    project_list = "\n".join(["- " + name for name in projects_data.keys()])
    await message.answer(f"Available projects:\n{project_list}")

@dp.message(Command("random"))
async def random_post(message: Message):
    print(f"🔔 Received /random from {message.from_user.username}")
    valid_projects = [key for key in projects_data if projects_data[key]]
    if not valid_projects:
        await message.answer("😞 Немає доступних постів.")
        return
    project = random.choice(valid_projects)
    post = random.choice(projects_data[project])
    await message.answer_photo(post["image"], caption=f"[{project.title()}]\n{post['text']}")

@dp.message(Command("post"))
async def post_handler(message: Message):
    print(f"🔔 Received /post from {message.from_user.username}")
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("⚠️ Вкажіть назву проєкту. Наприклад: /post linera")
        return

    project = args[1].strip().lower()
    posts = projects_data.get(project)
    if not posts:
        await message.answer("❌ Невідомий проєкт. Перевірте список: /list_projects")
        return

    post = random.choice(posts)
    await message.answer_photo(post["image"], caption=f"[{project.title()}]\n{post['text']}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
