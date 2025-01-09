import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Твой токен BotFather
API_TOKEN = 'YOUR_TOKEN'

# Инит бота в диспетчере
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# Обработка команды /start
@dp.message(Command(commands=['start']))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Я ваш бот.")

# Функция запуска бота
async def main():
    await dp.start_polling(skip_updates=True)

# Запуск бота
if __name__ == '__main__':
    asyncio.run(main())
