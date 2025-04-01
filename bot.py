
import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ChatMemberUpdated
from aiogram.utils import executor

TOKEN = os.getenv("7685134445:AAHtElPXRlF-EOXDw8fcV681hXTNyUWnDiA")
CHANNEL_ID = os.getenv("@cringememyukr")

if not TOKEN:
    raise ValueError("❌ Ошибка: Переменная окружения TOKEN не установлена! Проверьте Railway.")
if not CHANNEL_ID:
    raise ValueError("❌ Ошибка: Переменная окружения CHANNEL_ID не установлена! Проверьте Railway.")

bot = Bot(token=TOKEN, parse_mode="Markdown")
dp = Dispatcher(bot)

# Когда пользователь присоединился или отписался от канала
@dp.chat_member()
async def on_user_status_change(event: ChatMemberUpdated):
    # Если пользователь присоединился
    if event.new_chat_member.status == "member":
        chat = await bot.get_chat(CHANNEL_ID)
        count = await bot.get_chat_members_count(CHANNEL_ID)
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=f"На каналі *{chat.title}* нарахували *{count}* геїв",
            disable_notification=False
        )
    # Если пользователь покидает канал
    elif event.new_chat_member.status == "left":
        chat = await bot.get_chat(CHANNEL_ID)
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text="Хтось став натуралом",
            disable_notification=False
        )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
