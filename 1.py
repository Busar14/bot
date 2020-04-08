import telebot
import config
import random
 
from telebot import types
TOKEN="1205511771:AAGazab8n7_GqdKwUtgiUoW6-MAy3GV--f4"
bot = telebot.TeleBot(TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):
    
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Macdonald's  🍔")
    item2 = types.KeyboardButton("KFC 🍗")
    item3 = types.KeyboardButton("Шаурма 🌯")
    item4 = types.KeyboardButton("Пицца 🍕")
 
    markup.add(item1, item2, item3, item4)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы собирать данные по заказам 'Сливочек'\n Где сегодня хочешь поесть?".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == "Macdonald's  🍔":
            bot.send_message(message.chat.id, " ✌ Замечательно, скинь мне что именно ты хочешь заказать, а затем переведи МАНИ $. И незабудь про доставку )\n Вот реквезит кары :\n💳 +7 999-109-42-01")
        
        
        elif message.text == "KFC 🍗":
            bot.send_message(message.chat.id, " ✌ Замечательно, скинь мне что именно ты хочешь заказать, а затем переведи МАНИ $. И незабудь про доставку )\n Вот реквезит кары :\n💳 +7 999-109-42-01")


        elif message.text == "Шаурма 🌯":
            bot.send_message(message.chat.id, "Здравый выбор, Бусар тебя потдерживает! Скинь мне что именно ты хочешь заказать, а затем переведи МАНИ $. И незабудь про доставку )\n Вот реквезит кары :\n💳 +7 999-109-42-01")

        elif message.text == "Пицца 🍕":
            bot.send_message(message.chat.id, " ✌ Замечательно, скинь мне что именно ты хочешь заказать, а затем переведи МАНИ $. И незабудь про доставку )\n Вот реквезит кары :\n💳 +7 999-109-42-01")

        
        else:
            bot.send_message(message.chat.id,'Эй парень, я тебя не понимаю 🤨\nСделано специальное меню, а ты пишешь мне какую-то Хуйню!\nПо-моему тебе надо в другую группу\n😂 Сливочки явно не для тебя 😂')
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
 
            markup.add(item1, item2)
 
            
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)