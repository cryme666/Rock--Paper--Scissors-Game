import telebot
from telebot import types
from dotenv import load_dotenv
import os
import random

# emoj = {
#     '🪨': "камінь",
#     '✂️': "папір",
#     '📄': "ножниці"
# }

list = ["🪨", "📄", "✂️"]

load_dotenv()
API_KEY = os.getenv("API_KEY")

bot = telebot.TeleBot(API_KEY)

bot_commands = {
    '/help': 'Список команд',
    '/start_game': 'Почати гру',
    '/admin': 'ID розробника',
    
}

admins = [
    655826401,
    719626894
]

images = {
    'welcome': 'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmRoNDc5NDUzcXV6ZjhyNDBlcW00a2czOW5ia2tqbzVjN3F6Z2IyYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IzKrzRa01oB2KkvC7I/giphy.gif',
    'choose': 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnZycGE2ZzNlNWlwYm9manExN3NyMHh5cWJiZGw3dGdpM204eXJ4dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/eaDai9TQ2o1LKCj8xT/giphy.gif',
    'win': 'https://64.media.tumblr.com/b675b4f06b080a76fc6fc2dd42234588/tumblr_nx9gh7GkDT1rwfctbo2_500.gifv',
    'lose': 'https://64.media.tumblr.com/8da8f386f2820e3be033524e19d1634d/tumblr_nx9gh7GkDT1rwfctbo3_500.gifv',
    'friendship': 'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2Rnczlmb243ZjlocTNhanJoanMxYTl4bGZ2ZGM0cXFmNTVmcTJhbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VhRU9RvKZWKujYXhlJ/giphy.gif',
    'commands': 'https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExanBwZTFlcXF0NG9tbmY2ODZqaHZxemJvM2lsOXQ1NGh3aHN1eHVtbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L2KeF62rjXMyIZ7GMu/giphy.gif',
    'error': 'https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWs2YWpmZXlkNDk2NWQzeW5hOXJpNGJ0ZWpucjVydHNvZmc0bXJ6YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/elPGI1VakLYmuPKPmE/giphy.gif'
}

@bot.message_handler(commands=['start'])
def start(message):
    #todo write normal msg with gif
    caption = f'<b>Привіт! Давай пограємо в гру:\n"Камінь-Ножниці-Папір"!</b>'
    bot.send_animation(message.chat.id, images['welcome'], caption=caption, parse_mode='HTML')

@bot.message_handler(commands=['help'])
def help(message):
    caption = ( f"<b>Давай допоможу!\nОсь всі доступні тобі команди:</b>\n" +
            '\n'.join([f'{command}:  {descrption}' for command, descrption in bot_commands.items()]) )
    bot.send_animation(message.chat.id, images['commands'], caption=caption, parse_mode='HTML')  

@bot.message_handler(commands=['start_game'])
def start_game(message):
    
    itembtn1 = types.KeyboardButton('🪨')
    itembtn2 = types.KeyboardButton('✂️')  
    itembtn3 = types.KeyboardButton('📄')

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

@bot.message_handler(func = lambda message: True)
def echo_all(message):
    human_choice = message.text.lower()
    if human_choice in list:
        сomputer_choice = random.choice(list)
        ishumanwins = play_game(human_choice,сomputer_choice)
        caption = f'''Користувач вибрав\t{human_choice}.\nОпонент вибрав\t{сomputer_choice}.
        <b>{ishumanwins}</b>
        '''
        img_who_win = images['win'] if ishumanwins == "Переміг гравець!" else images['lose'] if ishumanwins == "Переміг опонент!" else images['friendship']
        bot.send_animation(message.chat.id, img_who_win, caption=caption, parse_mode='HTML')
    else: 
        caption = f'<b>На жаль я не знаю таких команд(</b>'
        bot.send_animation(message.chat.id, images['error'], caption=caption, parse_mode='HTML')

def play_game(human_choice,сomputer_choice):
     if human_choice == сomputer_choice:
        return "Перемогла дружба!"
        # number_of_ties += 1
     elif human_choice == "✂️" and сomputer_choice == "📄":
        # print("Переміг гравець!")
        # human_score += 1
        return "Переміг гравець!"

     elif human_choice == "📄" and сomputer_choice == "🪨":
        # print("Переміг гравець!")
        # human_score += "Переміг гравець!"
        return "Переміг гравець!"

     elif human_choice == "🪨" and сomputer_choice == "✂️":
        # print("Переміг гравець!")
        # human_score += "Переміг гравець!"
        return "Переміг гравець!"

     else:
        # print("Переміг опонент!")
        # computer_score += 1
        return "Переміг опонент!"




def bot_turn_on(chat_id = -4256691710):
    bot.send_message(chat_id,"Бот вкл.")
    bot.polling(non_stop=True)

if __name__ == "__main__":
    bot_turn_on()



