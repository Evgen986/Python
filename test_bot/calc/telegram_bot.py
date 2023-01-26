from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands


def start_bot():
    app = ApplicationBuilder().token("5841865362:AAGe-mekNEv9gYIPrV8kxAA6eNihfpSGJrU").build()

    app.add_handler(CommandHandler("count", bot_commands.count_command))
    # app.add_handler(CommandHandler("help", bot_commands.help_command))

    print('Сервер запустился')
    app.run_polling()
