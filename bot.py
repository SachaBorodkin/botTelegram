import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ChatMemberUpdated
from aiogram.filters import ChatMemberUpdatedFilter

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("@cringememyukr")

bot = Bot(token=TOKEN, parse_mode="Markdown")
dp = Dispatcher()

@dp.chat_member(ChatMemberUpdatedFilter(member_status_changed=True))
async def on_user_join(event: ChatMemberUpdated):
    if event.new_chat_member.status == "member":
        chat = await bot.get_chat(CHANNEL_ID)
        count = await bot.get_chat_members_count(CHANNEL_ID)
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=f"На каналі *{chat.title}* нарахували *{count}* геїв",
            disable_notification=False
        )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
