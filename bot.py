import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Botingiz tokini
API_TOKEN = '8346170407:AAGQyIvFu5I3ZTx0ZQ9rIlF7bc6nhBF7mus'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Menyu tugmalari
def main_menu():
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="Isming nima?"))
    builder.row(types.KeyboardButton(text="Yordam"), types.KeyboardButton(text="Adminga yozish"))
    return builder.as_markup(resize_keyboard=True)

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Salom! Behruz_Ai botiga xush kelibsiz. Quyidagi menyudan foydalaning:", 
                        reply_markup=main_menu())

@dp.message()
async def echo(message: types.Message):
    if message.text == "Isming nima?":
        await message.answer("Mening ismim Behruz_Ai.")
    elif message.text == "Yordam":
        await message.answer("Sizga qanday yordam bera olaman? Muammo bo'lsa adminga murojaat qiling.")
    elif message.text == "Adminga yozish":
        await message.answer("Admin bilan bog'lanish: @BehruzAibot")
    else:
        await message.answer(f"Siz yozdingiz: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
