# Bot para telegram by Rosso, Daniel Alberto

import telebot
import time
from pyspectator import cpu
from API_CONF import token

API_TOKEN = token.API_TOKEN
try:
    bot = telebot.TeleBot(API_TOKEN)
    bienvenida = "Bienvenido al Bot con el que interacturá para obtener la información del servidor.̣"
    stat = "El comando /online le permitirá acceder a ella."
    tempe = "El comando /temp permitirá conocer la temperatura del servidor."
except:
    print('API not valid!!')
# Handle '/start'
try:
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.chat.id, bienvenida + '\n' + stat + '\n' + tempe);
        chatid = message.chat.id


    # Handle '/online'
    @bot.message_handler(commands=['online'])
    def send_online(message):
        while True:
            bot.send_message(message.chat.id, "Este servidor esta online");
            time.sleep(600)

    #Handle '/temp'
    @bot.message_handler(commands=['temperatura'])
    def send_online(message):
        while True:
            bot.send_message(message.chat.id, "La temperatura es de: " + cpu.temperature);


    bot.polling()
except:
    print('Error handle')
