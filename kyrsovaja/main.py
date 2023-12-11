import telebot
import requests
import json

bot = telebot.TeleBot('6905023146:AAG28CavmEk-NUC359ytTNhqdah89-yH8ls')
WeatherAPI = '1a8379df8ce25e47689b8f0ae2383d8b'

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет! {message.from_user.first_name}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>/start</b> - Запускает бота \n/<b>status</b> - Показывает статус бота \n<b>/weather</b> - Напишет погоду', parse_mode='html')
@bot.message_handler(commands=['status'])
def main(message):
    bot.send_message(message.chat.id, 'Бот работает')

@bot.message_handler(commands=['weather'])
def weather(message):
    bot.send_message(message.chat.id, 'Напиши свой город что бы я мог помочь!')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WeatherAPI}&units=metric')
    data = json.loads(res.text)
    temp = data["main"]["temp"]
    windspeed = data["wind"]["speed"]
    bot.reply_to(message, f'Сейчас температура: {temp}' + 'C' + '\n' f'скорость ветра: {windspeed}')
    image = 'cold.png' if temp > 5.0 else 'sun.png'
    file = open('./' + image, 'rb')
    bot.send_photo(message.chat.id, file)
@bot.message_handler()
def userinput(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет! {message.from_user.first_name}')
    elif message.text.lower() == 'помощь':
        bot.send_message(message.chat.id, '<b>/start</b> - Запускает бота \n/<b>status</b> - Показывает статус бота', parse_mode='html')

bot.polling(none_stop=True)