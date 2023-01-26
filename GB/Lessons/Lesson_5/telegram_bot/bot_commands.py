from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import time
from spy import *


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(time.strftime('%H:%M'))


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi - приветствие;\n/time - узнать время;\n'
                                    f'/help - запросить список команд;\n/sum - сложить две цифры')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    await update.message.reply_text(f'{items[1]}+{items[2]}={int(items[1]) + int(items[2])}')
