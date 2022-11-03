import telebot
from telebot import types
import random


bot=telebot.TeleBot('5637218189:AAG-zdzzAZEHObVDkYuRCLMLs0YLT_Zya9c')

@bot.message_handler(commands=['start'])
def start_message(message):
    mess = f'<i>Привет</i>, <b>{message.from_user.first_name}</b>! \n \n  <b>Давай поиграем?</b> '
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Давай', callback_data=1))
    markup.add(types.InlineKeyboardButton(text='Не хочу', callback_data=2))
    bot.send_message(message.chat.id, mess , parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за  твой выбор !')
    answer = ''
    if call.data == '1':
        answer = 'А поиграем мы с тобой в : \n  камень \u270a ножницы \u270c\ufe0f бумага  \u270b  \n Команда /play запустит игру '

    elif call.data == '2':
        answer = f' <b>Жаль! \n Передумаешь, заходи!</b>'

    bot.send_message(call.message.chat.id, answer, parse_mode='html')

@bot.message_handler(commands=['play'])
def get_user_text (message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Камень \u270a')
    btn2 = types.KeyboardButton('Ножницы \u270c\ufe0f')
    btn3 = types.KeyboardButton('Бумага \u270b')
    keyboard.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'Твой выбор:',reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def game(message):
    choice = random.choice(['Камень \u270a', 'Ножницы \u270c\ufe0f', 'Бумага \u270b'])
    if message.text == choice:
       bot.send_message(message.chat.id, 'А у нас ничья ! Для начала новой игры нажми /play')
    else:
        if message.text == 'Камень \u270a':
            if choice == 'Ножницы \u270c\ufe0f':
                bot.send_message(message.chat.id,f'Вы победили! Бот выбрал: {choice} \n Для начала новой игры нажми /play')
            else:
               bot.send_message(message.chat.id,f'Вы проиграли!  Бот выбрал: {choice} \n Для начала новой игры нажми /play')

        if message.text == 'Ножницы \u270c\ufe0f':
            if choice == 'Бумага \u270b':
               bot.send_message(message.chat.id,f'Вы победили! Бот выбрал: {choice} \n Для начала новой игры нажми /play')

            else:
                bot.send_message(message.chat.id,f'Вы проиграли!  Бот выбрал: {choice} \n Для начала новой игры нажми /play')


        if message.text == 'Бумага \u270b':
            if choice == 'Камень \u270a':
                    bot.send_message(message.chat.id,f'Вы победили! Бот выбрал: {choice} \n Для начала новой игры нажми /play')

            else:
                    bot.send_message(message.chat.id,f'Вы проиграли! Бот выбрал: {choice} \n Для начала новой игры нажми /play')


bot.polling(none_stop=True)









    # if message.text.lower() == 'бумага':
    #     markup = types.InlineKeyboardMarkup(row_width=3)
    #     itembtn1 = types.InlineKeyboardButton(text='камень \u270a', callback_data='камень')
    #     itembtn2 = types.InlineKeyboardButton(text='ножницы \u270c\ufe0f', callback_data='ножницы')
    #     itembtn3 = types.InlineKeyboardButton(text='бумага \u270b', callback_data='бумага')
    #     markup.add(itembtn1, itembtn2, itembtn3)
    #
    #     bot.send_message(message.chat.id, "Верно! Твой ход:", reply_markup=markup)
    #
    #  else:
    #     markup = types.InlineKeyboardMarkup(row_width=3)
    #     itembtn1 = types.InlineKeyboardButton(text='камень  \u270a', callback_data='камень')
    #     itembtn2 = types.InlineKeyboardButton(text='ножницы \u270c\ufe0f', callback_data='ножницы')
    #     itembtn3 = types.InlineKeyboardButton(text='бумага  \u270b', callback_data= 'бумага')
    #     markup.add(itembtn1, itembtn2, itembtn3)
    #
    #     bot.send_message(message.chat.id, "Это бумага! Твой ход:", reply_markup=markup)
    #


# @bot.callback_query_handler(func=lambda call: call.data in ['камень', 'ножницы', 'бумага'])
# def choice_user(call):
#     knb= random.choice(["камень", "ножницы", "бумага"])
#
#     bot.answer_callback_query(callback_query_id=call.id, text='Ваш ход принят!')
#     bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                           text=f"Вы выбрали: {call.data}", reply_markup=None)




# @bot.message_handler(content_types=['text'])
# def game(message):
#     choice = random.choice(['Камень \u270a', 'Ножницы \u270c\ufe0f', 'Бумага \u270b'])
#     win = {'Камень\u270a': 'Ножницы\u270c\ufe0f', 'Ножницы\u270c\ufe0f': 'Бумага\u270b', 'Бумага\u270b': 'Камень\u270a'}
#
#     if message.text == choice:
#         bot.send_message(message.chat.id, 'А у нас ничья ! Для начала новой игры нажми /play')
#     if win[message] == choice:
#         bot.send_message(message.chat.id, f'Вы победили! Бот выбрал: {choice} \n Для начала новой игры нажми /play')
#
#     else:
#         bot.send_message(message.chat.id, f'Вы проиграли! Бот выбрал: {choice} \n Для начала новой игры нажми /play')
#
