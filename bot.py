import telebot
from telebot import types
from dotenv import load_dotenv
import os
import random

# emoj = {
#     '✊🏻': "камінь",
#     '✌🏻': "папір",
#     '✋🏻': "ножниці"
# }

list = ["✊🏻", "✋🏻", "✌🏻"]

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

images = {
    'welcome': 'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmRoNDc5NDUzcXV6ZjhyNDBlcW00a2czOW5ia2tqbzVjN3F6Z2IyYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IzKrzRa01oB2KkvC7I/giphy.gif',
    'choose': 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnZycGE2ZzNlNWlwYm9manExN3NyMHh5cWJiZGw3dGdpM204eXJ4dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/eaDai9TQ2o1LKCj8xT/giphy.gif',
    
}

@bot.message_handler(commands=['start'])
def start(message):
    #todo write normal msg with gif
    caption = f'<b>Привіт! Давай пограємо в гру:\n"Камінь-Ножниці-Папір"!</b>'
    bot.send_animation(message.chat.id, images['welcome'], caption=caption, parse_mode='HTML')

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, f"Список команд:\n{bot_commands}")

@bot.message_handler(commands=['start_game'])
def start_game(message):
    
    itembtn1 = types.KeyboardButton('✊🏻')
    itembtn2 = types.KeyboardButton('✌🏻')  
    itembtn3 = types.KeyboardButton('✋🏻')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(itembtn1, itembtn2, itembtn3)
    #todo add gif
    bot.send_animation(message.chat.id, images['choose'], 
                       caption="<b>Виберіть кнопку:</b>",
                       reply_markup=markup, parse_mode='HTML')

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
    human_choice = message.text.lower()
    if human_choice in list:
        сomputer_choice = random.choice(list)
        # ishumanwins = play_game(human_choice,сomputer_choice)
        # caption = f'''Користувач вибрав {human_choice}
        # Опонент вибрав {сomputer_choice}
        # '''
        bot.reply_to(message,play_game(human_choice,сomputer_choice))
        
    else:
        bot.reply_to(message,"На жаль я не знаю таких команд(")


def play_game(human_choice,сomputer_choice):
     if human_choice == сomputer_choice:
        return 0
        # number_of_ties += 1
     elif human_choice == "✌🏻" and сomputer_choice == "✌🏻":
        # print("Переміг гравець!")
        # human_score += 1
        return 1

     elif human_choice == "✌🏻" and сomputer_choice == "✊🏻":
        # print("Переміг гравець!")
        # human_score += 1
        return 1

     elif human_choice == "✊🏻" and сomputer_choice == "✌🏻":
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



