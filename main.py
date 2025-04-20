
import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer("👋 Добро пожаловать в InviteCashBot!

Для начала работы введите промокод или пополните баланс.")

@dp.message_handler(commands=["admin"])
async def admin_cmd(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("🔐 Панель администратора: здесь будут функции управления.")
    else:
        await message.answer("⛔️ У вас нет доступа к админке.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
