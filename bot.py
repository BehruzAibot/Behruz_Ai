import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
import yt_dlp

# Faqat Telegram Bot Token kerak
API_TOKEN = '8346170407:AAGQyIvFu5I3ZTx0ZQ9rIlF7bc6nhBF7mus'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Video yuklash funksiyasi (API-siz)
def download_video_direct(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': 'video.mp4',
        'quiet': True,
        'no_warnings': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return 'video.mp4'

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Salom! Menga TikTok, Instagram yoki YouTube linkini yuboring, men uni API-larsiz yuklab berishga harakat qilaman!")

@dp.message(F.text.contains("instagram.com") | F.text.contains("tiktok.com") | F.text.contains("youtube.com") | F.text.contains("youtu.be"))
async def handle_docs(message: types.Message):
    url = message.text
    wait_msg = await message.answer("⏳ Video yuklanmoqda (bu biroz vaqt olishi mumkin)...")
    
    try:
        # Videoni serverga yuklab olish
        loop = asyncio.get_event_loop()
        video_file = await loop.run_in_executor(None, download_video_direct, url)
        
        # Videoni foydalanuvchiga yuborish
        video = types.FSInputFile(video_file)
        await message.answer_video(video=video, caption="✅ Marhamat!")
        await wait_msg.delete()
        
        # Faylni o'chirish (joyni tejash uchun)
        if os.path.exists(video_file):
            os.remove(video_file)
            
    except Exception as e:
        await message.answer(f"❌ Xatolik yuz berdi. Bu linkdan video ololmadim.")
        print(f"Xato: {e}")

@dp.message()
async def echo(message: types.Message):
    await message.answer("Menga video linkini yuboring. Hozircha suhbatlashish funksiyasi o'chirilgan (chunki Gemini API ishlatilmayapti).")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
