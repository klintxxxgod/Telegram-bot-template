import telepot
from telepot.loop import MessageLoop

# Твой токен BotFather
API_TOKEN = 'YOUR_API_TOKEN'

# Инит бота
bot = telepot.Bot(API_TOKEN)

# Обработчик msg
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    if command == '/start':
        bot.sendMessage(chat_id, "Привет! Я ваш бот.")

# Запускаем бота
MessageLoop(bot, handle).run_as_thread()
print("Бот работает...")

# Оставляем программу запущенной
import time
while True:
    time.sleep(10)