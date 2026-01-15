import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

API_TOKEN = '8346170407:AAGQyIvFu5I3ZTx0ZQ9rIlF7bc6nhBF7mus'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Oddiy menyu tugmalari
def main_menu():
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="Isming nima?"))
    builder.row(types.KeyboardButton(text="Yordam"), types.KeyboardButton(text="Biz haqimizda"))
    return builder.as_markup(resize_keyboard=True)

# Xabar tagidagi (Inline) tugma
def inline_menu():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Kanalimizga o'tish", url="https://t.me/BehruzAibot"))
    return builder.as_markup()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Salom! Yangilangan Behruz_Ai botiga xush kelibsiz!", reply_markup=main_menu())

@dp.message()
async def handle_messages(message: types.Message):
    if message.text == "Isming nima?":
        await message.answer("Mening ismim Behruz_Ai. Men serverda yashayman!")
    elif message.text == "Yordam":
        await message.answer("Sizga qanday yordam kerak? Adminga murojaat qiling: @BehruzAibot")
    elif message.text == "Biz haqimizda":
        # Bu yerda bot rasm va inline tugma yuboradi
        photo_url = "https://picsum.photos/400/200" # Tasodifiy rasm manzili
        await message.answer_photo(
            photo=photo_url, 
            caption="Bu bizning loyiha haqida qisqacha ma'lumot. Pastdagi tugmani bosing:",
            reply_markup=inline_menu()
        )
    else:
        await message.answer(f"Siz yozdingiz: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
