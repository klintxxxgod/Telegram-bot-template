import telebot

# Твой токен BotFather
API_TOKEN = 'YOUR_API_TOKEN'

# Инит бота
bot = telebot.TeleBot(API_TOKEN)

# Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я ваш бот.")

# Запускаем бота
if __name__ == '__main__':
    bot.polling()