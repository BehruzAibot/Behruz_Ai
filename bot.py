import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Tokenni tekshiring
API_TOKEN = '8346170407:AAGQyIvFu5I3ZTx0ZQ9rIlF7bc6nhBF7mus'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Salom! Mening ismim Behruz_Ai. Sizga qanday yordam bera olaman?")

@dp.message()
async def echo(message: types.Message):
    if "isming nima" in message.text.lower():
        await message.answer("Mening ismim Behruz_Ai.")
    else:
        await message.answer("Xabaringizni qabul qildim!")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__' :
    asyncio.run(main())