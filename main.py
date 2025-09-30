import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from handlers import router
from database import create_db
from config import BOT_TOKEN

async def main():
    ''' Initialize bot and dispatcher '''
    await create_db()
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

print('Bot is running...')
if __name__ == "__main__":
    asyncio.run(main())