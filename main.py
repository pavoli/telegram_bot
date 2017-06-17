# coding: utf8

import telebot
import constants

bot = telebot.TeleBot(constants.token)
#bot.send_message(chat_id=285275745, text="test")
upd = bot.get_updates()
#print upd

#last_upd = upd[-1]
#message_from_user = last_upd.message
#print message_from_user

def log(message, answer):
    print u"\n ----------"
    from datetime import datetime
    print datetime.now()
    print u"Сообщение от {0} {1}. (id={2} \n Текст - {3})".format(message.from_user.first_name,
                                                              message.from_user.last_name,
                                                              str(message.from_user.id),
                                                              message.text)
    print answer

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    user_markup.row('/start', '/stop')
    user_markup.row(u'фото', u'аудио', u'документы')
    user_markup.row(u'стикер', u'видео', u'голос', u'локация')
    bot.send_message(message.from_user.id, u'Добро пожаловать!', reply_markup=user_markup)

@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, u'...', reply_markup=hide_markup)


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, """Мои возможности ограничены пока
    Но ты только посмотри,- все работает!!!""")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = u"Что-то пошло не так..."
    if message.text == u"а":
        answer = u"Б"
        log(message, answer)
        bot.send_message(message.chat.id, answer)
    elif message.text == u"б":
        answer = u"В"
        log(message, answer)
        bot.send_message(message.chat.id, answer)
    else:
        log(message, answer)
        bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True, interval=0)