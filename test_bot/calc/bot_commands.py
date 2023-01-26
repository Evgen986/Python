from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import model_racional as mr
import user_interfeice as ui


# from spy import *


async def count_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # log(update, context)
    print(update.message.text)
    msg = update.message.text.split()
    print(msg[1])
    text, text_list = ui.get_nums(msg[1])
    await update.message.reply_text(f'{text} = {mr.get_result(text_list)}')

# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     # log(update, context)
#     await update.message.reply_text(f'/hi - приветствие;\n/time - узнать время;\n'
#                                     f'/help - запросить список команд;\n/sum - сложить две цифры')
