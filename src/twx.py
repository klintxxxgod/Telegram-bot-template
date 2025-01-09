from twx.botapi import Bot, TelegramAPIError
import logging

# Твой токен BotFather
API_TOKEN = 'YOUR_API_TOKEN'

# Включение логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Создаем экземпляр бота
bot = Bot(API_TOKEN)

async def main():
    # Получение информации о боте
    try:
        await bot.get_me()
        print("Бот успешно запущен.")
    except TelegramAPIError as e:
        print(f"Ошибка при запуске бота: {e}")

    # Обработка новых сообщений
    async def handle_new_messages(updates):
        for update in updates:
            if update.message and update.message.text == '/start':
                await bot.send_message(chat_id=update.message.chat.id, text='Привет! Я ваш бот.')

    # Запуск бота
    await bot.polling(handle_new_messages)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())