import telebot
from telebot import types
from dotenv import load_dotenv
import os
from game_logic import play_game
from utils import *
from user_managing import check_user


load_dotenv()
API_KEY = os.getenv("API_KEY")

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    user_name = message.from_user.username 
    user_data = {"id": str(user_id), "username":user_name}
    check_user(user_data)

    caption = f'<b>Привіт! Давай пограємо в гру:\n"Камінь-Ножниці-Папір"!</b>'
    bot.send_animation(message.chat.id, images['welcome'], caption=caption, parse_mode='HTML')

@bot.message_handler(commands=['help'])
def help(message):
    caption = ( f"<b>Давай допоможу!\nОсь всі доступні тобі команди:</b>\n" +
            '\n'.join([f'{command}:  {descrption}' for command, descrption in bot_commands.items()]) )
    bot.send_animation(message.chat.id, images['commands'], caption=caption, parse_mode='HTML')  

@bot.message_handler(commands=['start_game'])
def start_game(message):
    
    itembtn1 = types.KeyboardButton(CHOICES[0])
    itembtn2 = types.KeyboardButton(CHOICES[1])  
    itembtn3 = types.KeyboardButton(CHOICES[2])

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(itembtn1, itembtn2, itembtn3)
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
    



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print("hello")
    human_choice = message.text.lower()
    if human_choice in CHOICES:
        result,computer_choice  = play_game(human_choice)
        caption = f'''Користувач вибрав {human_choice}.\nОпонент вибрав {computer_choice}.\n<b>{'Переміг гравець!' if result == 1 else 'Переміг опонент!' if result == -1 else 'Нічия!'}</b>'''
        img_who_win = get_winner_animation(result)
        bot.send_animation(message.chat.id, img_who_win, caption=caption, parse_mode='HTML')
    else: 
        caption = '<b>На жаль, я не розумію таких команд</b>'
        bot.send_animation(message.chat.id, images['error'], caption=caption, parse_mode='HTML')


def bot_turn_on(chat_id = -4256691710):
    bot.send_message(chat_id,"Бот вкл.")
    bot.polling(non_stop=True)

if __name__ == "__main__":
    bot_turn_on()



