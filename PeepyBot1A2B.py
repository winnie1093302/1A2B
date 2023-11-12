# from telegram.ext.updater import Updater
# from telegram.update import Update
from telegram.ext import CallbackQueryHandler
# from telegram.ext.callbackcontext import CallbackContext
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
# from telegram.ext.commandhandler import CommandHandler
# from telegram.ext.messagehandler import MessageHandler
from telegram.ext import Filters
from telegram import Update
from telegram.ext import Updater, CallbackContext
from telegram.ext import MessageHandler, CommandHandler, InlineQueryHandler, CallbackQueryHandler
import random
import words3
import words4
import words5
import words6

import time
import os

level = ['3', '4', '5', '6']

emoji = {
    0 :'easy',
    1 :'medium',
    2 :'hard',
    3 :'super hard' 
}

global answer
answer = ''

updater = Updater("6963019610:AAG605ZJMFsOgAXs-8eJ1BEnPwEuSK_yGmI",use_context=True)
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello {}, It's Peppy here~\
        \nPlease write '/wordle' to start Wordle Game^^".format(update.message.from_user.first_name))

def hello(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Hello, {}!'.format(update.message.from_user.first_name))

def wordle(update: Update, context: CallbackContext) :
        update.message.reply_text('Please choose the difficulty!',
         reply_markup = InlineKeyboardMarkup([[
                InlineKeyboardButton(emoji, callback_data = level) for level, emoji in emoji.items()
            ]]))

def play(update: Update, context: CallbackContext):
    global answer
    length = int(update.callback_query.data)
    update.callback_query.edit_message_text("Enter a word with length of {}".format(level[length]))
    if level[length] == '3':
        answer = random.choice(words3.word_list)
        print(answer)
        updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_message3))
    elif level[length] == '4':
        answer = random.choice(words4.word_list)
        print(answer)
        updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_message4))
    elif level[length] == '5':
        answer = random.choice(words5.word_list)
        print(answer)
        updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_message5))
    elif level[length] == '6':
        answer = random.choice(words6.word_list)
        print(answer)
        updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_message6))

def handle_message3(update : Update, context: CallbackContext):
    user_ans = []

    for i in range(0, 3):
        user_ans.append("_")

    guess = update.message.text.lower()
    A = 0
    B = 0
    
    if len(guess) == 3:
        for j in range(0,3):
            if guess[j] == answer[j]:
                user_ans[j] = guess
                A=A+1
            for k in range(0,3):
                if guess[j] != answer[j] and guess[k] == answer[j]:
                    B=B+1
            
        update.message.reply_text(f'{A}A{B}B')
        if A == 3:
            update.message.reply_text('恭喜你答對了')
            updater.stop()
    else:
        update.message.reply_text('請輸入三個字的單詞')
                
def handle_message4(update : Update, context: CallbackContext):
    user_ans = []

    for i in range(0, 4):
        user_ans.append("_")

    guess = update.message.text.lower()
    A = 0
    B = 0
    
    if len(guess) == 4:
        for j in range(0,4):
            if guess[j] == answer[j]:
                user_ans[j] = guess
                A=A+1
            for k in range(0,4):
                if guess[j] != answer[j] and guess[k] == answer[j]:
                    B=B+1
            
        update.message.reply_text(f'{A}A{B}B')
        if A == 4:
            update.message.reply_text('恭喜你答對了')
            updater.stop()
    else:
        update.message.reply_text('請輸入四個字的單詞')                
        
def handle_message5(update : Update, context: CallbackContext):
    user_ans = []

    for i in range(0, 5):
        user_ans.append("_")

    guess = update.message.text.lower()
    A = 0
    B = 0

    if len(guess) == 5:    
        for j in range(0,5):
            if guess[j] == answer[j]:
                user_ans[j] = guess
                A=A+1
            for k in range(0,5):
                if guess[j] != answer[j] and guess[k] == answer[j]:
                    B=B+1
            
        update.message.reply_text(f'{A}A{B}B')
        if A == 5:
            update.message.reply_text('恭喜你答對了')
            updater.stop()
    else:
        update.message.reply_text('請輸入五個字的單詞')

def handle_message6(update : Update, context: CallbackContext):
    user_ans = []

    for i in range(0, 6):
        user_ans.append("_")

    guess = update.message.text.lower()
    A = 0
    B = 0
    
    if len(guess) == 6:
        for j in range(0,6):
            if guess[j] == answer[j]:
                user_ans[j] = guess
                A=A+1
            for k in range(0,6):
                if guess[j] != answer[j] and guess[k] == answer[j]:
                    B=B+1
            
        update.message.reply_text(f'{A}A{B}B')
        if A == 6:
            update.message.reply_text('恭喜你答對了')
            updater.stop()

    else:
        update.message.reply_text('請輸入六個字的單詞')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('wordle', wordle))
updater.dispatcher.add_handler(CallbackQueryHandler(play))

updater.start_polling()

time.sleep(60)
os._exit(0)
