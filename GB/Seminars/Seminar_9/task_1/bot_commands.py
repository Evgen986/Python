from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def edit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.split()
    text = text[1:]
    text = ' '.join(el for el in text if 'абв' not in el)
    await update.message.reply_text(f'{text}')
