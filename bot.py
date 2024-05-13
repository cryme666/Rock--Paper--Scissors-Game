import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

bot = telebot.TeleBot(API_KEY)

bot_commands = [
    '/help',
    '/start_game',
    '/admin',
]

admins = [
    655826401,
    719626894
]

@bot.message_handler(commands=['start'])
def start(message):
    #todo write normal msg with gif
    bot.reply_to(message,"Привіт я бот")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, f"Список команд:\n{bot_commands}")

@bot.message_handler(commands=['start_game'])
def start_game(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Камінь')
    itembtn2 = types.KeyboardButton('Ножниці')  
    itembtn3 = types.KeyboardButton('Папір')
    #todo add gif
    bot.send_message(message.chat.id, "Виберіть кнопку:", reply_markup=markup)

@bot.message_handler(commands=['admin'])
def admin_parametres(message):
    username = message.from_user.username   
    user_id = message.from_user.id
    if user_id in admins:
        bot.send_message(message.chat.id, f'''@{username} id: {user_id}
chat id: {message.chat.id}
''')
    else:
        bot.send_message(message.chat.id, f"Ви не обладаєте правами адміністратора.")



@bot.message_handler(commands=['turn_off'])
def bot_turn_off(message, chat_id = -4256691710):
    if message.from_user.id in admins:
        bot.send_message(chat_id,"Бот викл.")
        bot.stop_polling()
    else:
        bot.send_message(message.chat.id, f"Ви не обладаєте правами адміністратора.")


def bot_turn_on(chat_id = -4256691710):
    bot.send_message(chat_id,"Бот вкл.")
    bot.polling(non_stop=True)

if __name__ == "__main__":
    bot_turn_on()



