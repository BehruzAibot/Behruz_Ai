import asyncio
import os
import requests
from aiogram import Bot, Dispatcher, types, F

API_TOKEN = '8346170407:AAGQyIvFu5I3ZTx0ZQ9rIlF7bc6nhBF7mus'
# RapidAPI dan olingan kalitni ishlatamiz
SOCIAL_API_KEY = os.getenv("SHAZAM_API_KEY") # Avvalgi kalitni ishlatsak ham bo'ladi

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(F.text.contains("instagram.com") | F.text.contains("tiktok.com") | F.text.contains("youtube.com"))
async def download_video(message: types.Message):
    url = message.text
    await message.answer("Video tayyorlanmoqda, iltimos kuting...")
    
    # Bu yerda API orqali videoni yuklash havolasini olamiz
    # Hozircha namunaviy javob:
    try:
        # Video yuklash logikasi shu yerda bo'ladi
        await message.answer_video(video=url, caption="Mana sizning videongiz!")
    except Exception as e:
        await message.answer("Kechirasiz, videoni yuklab bo'lmadi.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
