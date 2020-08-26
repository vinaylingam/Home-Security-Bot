# Bot UserName : HomeSecurityenderBot

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import time
import TOKEN

updater = Updater(token=TOKEN.token, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename = "logs.txt")

def start(update, context):
    logging.info("---"*50)
    logging.info(update)
    logging.info(str(update.message.chat_id)+", Name: "+update.message.from_user.first_name+", Command Handled: Start")
    if update.message.chat_id != 442498914 :
        context.bot.send_message(chat_id=442498914,text="Bot is contacted by {0}({1}), id = {2}".format(update.message.from_user.first_name,update.message.from_user.username,update.message.chat_id))
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello {}".format(update.message.from_user.first_name)+" Welcome to Home Security bot. i am at your service..! ")

def distance(update, context):
    print("distance..")
    logging.info("---"*50)
    logging.info(update)
    logging.info(str(update.message.chat_id)+", Name: "+update.message.from_user.first_name+", Command Handled: distance")
    if update.message.chat_id != 442498914 :
        context.bot.send_message(chat_id=442498914,text="Bot is contacted by {0}({1}), id = {2}".format(update.message.from_user.first_name,update.message.from_user.username,update.message.chat_id))
    context.bot.send_message(chat_id=update.message.chat_id, text="Distance = "+str(0)+" cm")

def temperature(update, context):
    print("temperature..")
    logging.info("---"*50)
    logging.info(update)
    logging.info(str(update.message.chat_id)+", Name: "+update.message.from_user.first_name+", Command Handled: distance")
    if update.message.chat_id != 442498914 :
        context.bot.send_message(chat_id=442498914,text="Bot is contacted by {0}({1}), id = {2}".format(update.message.from_user.first_name,update.message.from_user.username,update.message.chat_id))
    context.bot.send_message(chat_id=update.message.chat_id, text="Temperature = "+str(0)+" degrees")

def textHandler(update, context):
    logging.info("---"*50)
    logging.info(update)
    logging.info(str(update.message.chat_id)+", free text handled")
    if update.message.chat_id != 442498914 :
        context.bot.send_message(chat_id=442498914,text="Bot is contacted by {0}({1}), id = {2}".format(update.message.from_user.first_name,update.message.from_user.username,update.message.chat_id))
    context.bot.send_message(chat_id=update.message.chat_id, text="Robot is under development..! Please use commands..!")


start_handler = CommandHandler('start', start)
distance_handler = CommandHandler('distance', distance)
temp_handler = CommandHandler('temperature', temperature)
text_handler = MessageHandler(Filters.text, textHandler)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(distance_handler)
dispatcher.add_handler(temp_handler)
dispatcher.add_handler(text_handler)

updater.start_polling()