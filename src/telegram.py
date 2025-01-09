from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Функция для обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я ваш бот.')

# Основная функция
def main():
    # Инит токена бота
    updater = Updater("YOUR_TOKEN")

    # Инит диспетчера
    dispatcher = updater.dispatcher

    # Рег обработчика /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Запускаем бот
    updater.start_polling()

    # Бот будет работать до остановки
    updater.idle()

if __name__ == '__main__':
    main()