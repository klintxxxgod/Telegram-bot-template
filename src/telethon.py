from telethon import TelegramClient, events

# Замените эти значения на свои данные
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
bot_token = 'YOUR_BOT_TOKEN'

# Создаем экземпляр клиента бота
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply('Привет! Я ваш бот.')

# Запускаем клиент
print("Бот работает...")
client.run_until_disconnected()