import asyncio
import os
import requests
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
import google.generativeai as genai

# Kalitlar
API_TOKEN = '8346170407:AAGQyIvFu5I3ZTx0ZQ9rIlF7bc6nhBF7mus'
GEMINI_KEY = os.getenv("GEMINI_API_KEY") # Render'dan oladi
RAPID_KEY = "53238bd7dfmshf6287d7ef95f084p189ffajsn13728687bd87" # Sizning rasmingizdagi kalit

# Gemini sozlamasi
if GEMINI_KEY:
    genai.configure(api_key=GEMINI_KEY)
    gemini = genai.GenerativeModel('gemini-pro')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Salom! Video linkini yuboring yoki savol bering.")

@dp.message(F.text.contains("instagram.com") | F.text.contains("tiktok.com") | F.text.contains("youtube.com") | F.text.contains("youtu.be"))
async def download_video(message: types.Message):
    url = message.text
    wait_msg = await message.answer("⏳ Video tayyorlanmoqda...")
    
    api_url = "https://social-download-all-in-one.p.rapidapi.com/v1/social/autolink"
    headers = {
        "x-rapidapi-key": RAPID_KEY,
        "x-rapidapi-host": "social-download-all-in-one.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(api_url, json={"url": url}, headers=headers).json()
        video_link = response.get('url')
        
        if video_link:
            await message.answer_video(video=video_link, caption="✅ Marhamat!")
            await wait_msg.delete()
        else:
            await message.answer("❌ Videoni yuklab bo'lmadi.")
    except Exception:
        await message.answer("⚠️ API bilan bog'lanib bo'lmadi.")

@dp.message()
async def chat_with_ai(message: types.Message):
    try:
        res = gemini.generate_content(message.text)
        await message.answer(res.text)
    except Exception:
        await message.answer("Hozircha sun'iy intellekt ishlamayapti (Kalitni tekshiring).")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
