import telebot
from telebot import types
from dotenv import load_dotenv
import os
import random
list = ["камінь", "папір", "ножниці"]

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
    itembtn1 = types.KeyboardButton('Камінь')
    itembtn2 = types.KeyboardButton('Ножниці')  
    itembtn3 = types.KeyboardButton('Папір')

    markup = types.ReplyKeyboardMarkup(row_width=3)
    markup.add(itembtn1, itembtn2, itembtn3)
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

@bot.message_handler(func = lambda message: True )
def echo_all(message):
    msg = message.text.lower()
    if msg in list:
        bot.reply_to(message,play_game(msg))

    else:
        bot.reply_to(message,"На жаль я не знаю таких команд(")


def play_game(human_choice):
     сomputer_choice = random.choice(list)
     if human_choice == сomputer_choice:
        return 0
        # number_of_ties += 1
     elif human_choice == "ножниці" and сomputer_choice == "папір":
        # print("Переміг гравець!")
        # human_score += 1
        return 1

     elif human_choice == "папір" and сomputer_choice == "камінь":
        # print("Переміг гравець!")
        # human_score += 1
        return 1

     elif human_choice == "камінь" and сomputer_choice == "ножниці":
        # print("Переміг гравець!")
        # human_score += 1
        return 1

     else:
        # print("Переміг опонент!")
        # computer_score += 1
        return -1




def bot_turn_on(chat_id = -4256691710):
    bot.send_message(chat_id,"Бот вкл.")
    bot.polling(non_stop=True)

if __name__ == "__main__":
    bot_turn_on()



