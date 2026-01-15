import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Telegram bot tokiningiz
API_TOKEN = '8346170407:AAGQyIvFu5I3ZTx0ZQ9rIlF7bc6nhBF7mus'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Salom! Men Behruz_Ai sun'iy intellekt botiman. Menga istagan savolingizni bering!")

@dp.message()
async def ai_chat(message: types.Message):
    # Bu yerda bot foydalanuvchi xabarini oladi
    user_text = message.text.lower()
    
    await message.answer("O'ylayapman... 🤔") # Bot o'ylayotganini ko'rsatadi

    # Oddiy mantiqiy AI (Hozircha shunday, keyin API ulaymiz)
    if "salom" in user_text:
        reply = "Assalomu alaykum! Sizga qanday yordam bera olaman?"
    elif "isming nima" in user_text:
        reply = "Mening ismim Behruz_Ai. Men Python tilida yaratilganman."
    elif "nima qila olasan" in user_text:
        reply = "Men savollarga javob berishim, menyular ko'rsatishim va siz bilan suhbatlashishim mumkin."
    else:
        # Haqiqiy AI xizmatini ulashdan oldin bot xabarni qayta ishlaydi
        reply = f"Siz '{message.text}' dedingiz. Hozircha men o'rganish jarayonidaman, tez orada ChatGPT kabi aqlli bo'laman!"

    await message.answer(reply)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
