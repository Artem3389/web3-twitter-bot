
import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart, Command

API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'

projects_data = {'linera': [{'text': 'Linera is redefining blockchain scalability with parallel chains. The future of fast, secure infra is here. 🚀 #Linera #Web3 #Airdrop', 'image': 'https://cryptologos.cc/logos/linera-logo.png'}, {'text': 'Scalable, fast, and async — Linera is the game-changer you’ve been waiting for. Don’t miss the ride. 🔥 #Layer1 #Linera', 'image': 'https://cryptologos.cc/logos/linera-banner.jpg'}], 'nexus': [{'text': 'Nexus unlocks unified blockchain UX — bridging speed, modularity & decentralization. The future is cross-chain. 🌐 #Nexus #Blockchain', 'image': 'https://cryptologos.cc/logos/nexus-logo.png'}, {'text': 'Nexus is building the backbone of seamless multi-chain interaction. Are you ready? 💥 #Crypto #Web3', 'image': 'https://cryptologos.cc/logos/nexus-banner.jpg'}], 'arcium': [{'text': 'Arcium brings privacy-first infrastructure to Web3. ZK-powered, unstoppable. 🛡️ #ZK #Arcium #Web3Infra', 'image': 'https://cryptologos.cc/logos/arcium-logo.png'}, {'text': 'The future of confidential computing is here. Arcium is setting the new standard. 🔐 #Blockchain #Arcium', 'image': 'https://cryptologos.cc/logos/arcium-banner.jpg'}], 'taker protocol': [{'text': 'Taker Protocol is reshaping DeFi liquidity — unlocking real-world assets with utility. 🌉 #TakerProtocol #DeFi', 'image': 'https://cryptologos.cc/logos/taker-protocol-logo.png'}, {'text': 'RWAs meet DeFi. Taker Protocol makes assets tradable across chains. Game on. 🏦 #RWA #Crypto', 'image': 'https://cryptologos.cc/logos/taker-banner.jpg'}], 'huddle': [{'text': 'Huddle is revolutionizing decentralized meetings. Web3-native communication done right. 🎙️ #Huddle01 #Web3Tools', 'image': 'https://cryptologos.cc/logos/huddle-logo.png'}, {'text': 'Say goodbye to Web2 calls. Huddle brings you decentralized audio/video spaces. 📞 #Huddle #CryptoInfra', 'image': 'https://cryptologos.cc/logos/huddle-banner.jpg'}], 'nous research': [{'text': 'Nous is building the future of decentralized AI. Own your data, power your models. 🤖 #NousResearch #AIxWeb3', 'image': 'https://cryptologos.cc/logos/nous-logo.png'}, {'text': 'AI with transparency & ownership. Nous Research leads the next gen AI infra. 💡 #Web3AI #Nous', 'image': 'https://cryptologos.cc/logos/nous-banner.jpg'}], 'soundness': [{'text': 'Soundness is pioneering secure and scalable cryptographic frameworks for Web3. 🔐 #Soundness #ZK', 'image': 'https://cryptologos.cc/logos/soundness-logo.png'}, {'text': 'ZK made practical. Soundness is enabling privacy-preserving computation. 🧠 #Crypto #PrivacyTech', 'image': 'https://cryptologos.cc/logos/soundness-banner.jpg'}], 'op_net': [{'text': 'OP_NET powers resilient and open P2P infrastructure. No single point of failure. 🌍 #OP_NET #Decentralization', 'image': 'https://cryptologos.cc/logos/opnet-logo.png'}, {'text': 'A fully decentralized internet needs OP_NET. Join the network that can’t be stopped. ⚡ #Web3Infra #OPNET', 'image': 'https://cryptologos.cc/logos/opnet-banner.jpg'}], 'talus network': [{'text': 'Talus Network brings secure multiparty computation to blockchain. Privacy at scale. 🛡️ #Talus #MPC', 'image': 'https://cryptologos.cc/logos/talus-logo.png'}, {'text': 'Zero-trust coordination? Talus Network makes it real. Built for confidential blockchain ops. 🔒 #TalusNetwork', 'image': 'https://cryptologos.cc/logos/talus-banner.jpg'}], 'glider': [{'text': 'Glider accelerates cross-chain interactions with blazing-fast messaging protocols. 🚀 #Glider #Interoperability', 'image': 'https://cryptologos.cc/logos/glider-logo.png'}, {'text': 'Move assets and data faster than ever. Glider makes bridging seamless. 🌐 #Web3Tools #Glider', 'image': 'https://cryptologos.cc/logos/glider-banner.jpg'}], 'optimum': [{'text': 'Optimum is building optimized L2 infra with near-zero gas & high throughput. 🔧 #Optimum #Rollups', 'image': 'https://cryptologos.cc/logos/optimum-logo.png'}, {'text': 'The most efficient chain infra yet? Optimum redefines performance. ⚙️ #L2Solutions #Web3Infra', 'image': 'https://cryptologos.cc/logos/optimum-banner.jpg'}], 'seismic': [{'text': 'Seismic is shaking up consensus design — modular and high performance. 🌊 #Seismic #ConsensusLayer', 'image': 'https://cryptologos.cc/logos/seismic-logo.png'}, {'text': 'Meet Seismic: a consensus engine tuned for tomorrow’s blockchains. 🚧 #Web3Dev #SeismicProtocol', 'image': 'https://cryptologos.cc/logos/seismic-banner.jpg'}], 'anoma': [{'text': 'Anoma is building intent-centric architecture for truly private, composable DApps. 🧩 #Anoma #PrivacyFirst', 'image': 'https://cryptologos.cc/logos/anoma-logo.png'}, {'text': 'Programmable privacy & intents? Anoma is ahead of the curve. 🌀 #ModularBlockchain #Anoma', 'image': 'https://cryptologos.cc/logos/anoma-banner.jpg'}]}

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
