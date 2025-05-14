
import os
import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart, Command

API_TOKEN = os.getenv'7928598221:AAGL804MBVpa-91hmcXoUgvbljYd7rOFaJU'

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Welcome! Use /post [project_name] to get a Web3 tweet. Use /help to see all commands.")

@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer("""Available commands:
/post [project_name] — get a tweet post for a project
/random — get a random project post
/list_projects — see all available project names""")

@dp.message(Command("list_projects"))
async def list_projects(message: Message):
    project_list = "\n".join(["- " + name for name in projects_data.keys()])
    await message.answer(f"Available projects:\n{project_list}")

@dp.message(Command("random"))
async def random_post(message: Message):
    project = random.choice(list(projects_data.keys()))
    post = random.choice(projects_data[project])
    await message.answer_photo(post["image"], caption=f"[{project.title()}]\n" + post["text"])

@dp.message(Command("post"))
async def post_handler(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Please provide a project name, e.g. /post linera")
        return

    project = args[1].strip().lower()
    if project not in projects_data:
        await message.answer("Unknown project. Use /list_projects to see available options.")
        return

    post = random.choice(projects_data[project])
    await message.answer_photo(post["image"], caption=post["text"])

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
