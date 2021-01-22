# Bot para telegram by Rosso, Daniel Alberto

import telebot
import time

API_TOKEN = '1574011521:AAHkoqbM_-f2jUj6Ho7sqNeD05bUMynVdcw'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Bienvenido al Bot con el que interacturá para obtener la información del servidor.̣" + '\n' + "El comando /online le permitirá acceder a ella.");
    chatid = message.chat.id


# Handle '/online'
@bot.message_handler(commands=['online'])
def send_online(message):
    while True:
        bot.send_message(message.chat.id, "Este servidor esta online");
        time.sleep(600)

bot.polling()