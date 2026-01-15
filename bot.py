import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from openai import AsyncOpenAI # ChatGPT uchun

# Kalitlarni joylang
API_TOKEN = '8346170407:AAGQyIvFu5I3ZTx0ZQ9rIlF7bc6nhBF7mus'
OPENAI_API_KEY = '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'

client = AsyncOpenAI(api_key=OPENAI_API_KEY)
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message()
async def chat_with_gpt(message: types.Message):
    # Bot "o'ylayotganini" bildirish uchun
    await bot.send_chat_action(message.chat.id, "typing")
    
    # ChatGPT-ga so'rov yuborish
    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message.text}]
    )
    
    # Javobni foydalanuvchiga qaytarish
    await message.answer(response.choices[0].message.content)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

