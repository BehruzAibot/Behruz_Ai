import asyncio
import os
import requests
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
import google.generativeai as genai

# Kalitlar (Render-dagi Environment Variables-dan olinadi)
API_TOKEN = '8346170407:AAGQyIvFu5I3ZTx0ZQ9rIlF7bc6nhBF7mus'
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
VIDEO_API_KEY = os.getenv("VIDEO_API_KEY")

# Gemini sozlamasi
genai.configure(api_key=GEMINI_KEY)
gemini = genai.GenerativeModel('gemini-pro')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Salom! Menga Instagram, TikTok yoki YouTube linkini yuboring, men videoni yuklab beraman. Shuningdek, savollaringizga ham javob bera olaman!")

@dp.message(F.text.contains("instagram.com") | F.text.contains("tiktok.com") | F.text.contains("youtube.com"))
async def download_video(message: types.Message):
    url = message.text
    wait_msg = await message.answer("⏳ Video tayyorlanmoqda, kuting...")
    
    api_url = "https://social-download-all-in-one.p.rapidapi.com/v1/social/autolink"
    payload = {"url": url}
    headers = {
        "x-rapidapi-key": VIDEO_API_KEY,
        "x-rapidapi-host": "social-download-all-in-one.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(api_url, json=payload, headers=headers).json()
        video_link = response.get('url')
        
        if video_link:
            await message.answer_video(video=video_link, caption="✅ Marhamat!")
            await wait_msg.delete()
        else:
            await message.answer("❌ Videoni yuklab bo'lmadi. Linkni tekshiring.")
    except Exception:
        await message.answer("⚠️ Texnik xatolik yuz berdi.")

@dp.message()
async def chat_with_ai(message: types.Message):
    try:
        res = gemini.generate_content(message.text)
        await message.answer(res.text)
    except Exception:
        await message.answer("Hozircha javob bera olmayman.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
