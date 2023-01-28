from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands




app = ApplicationBuilder().token("5841865362:AAGe-mekNEv9gYIPrV8kxAA6eNihfpSGJrU").build()
print('Сервер запустился')

app.add_handler(CommandHandler("g_1", bot_commands.g_1))


app.run_polling()
