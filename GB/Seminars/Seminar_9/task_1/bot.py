from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands


app = ApplicationBuilder().token("5841865362:AAGe-mekNEv9gYIPrV8kxAA6eNihfpSGJrU").build()

app.add_handler(CommandHandler("edit", bot_commands.edit))
print('Сервер запустился')
app.run_polling()
