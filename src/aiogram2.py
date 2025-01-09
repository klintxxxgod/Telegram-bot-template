import logging
from aiogram2 import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

# Твой токен BotFather
API_TOKEN = 'YOUR_TOKEN'

# Инит бота в диспетчере
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Обработка команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я ваш бот.")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)