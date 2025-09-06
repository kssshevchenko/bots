from importlib.metadata import entry_points

from telegram import Update, BotCommand
import secrets
import string
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ConversationHandler, Application

symbols = f"{string.ascii_letters}{string.punctuation}{string.digits}"
length = 1

async def main(application: Application):
    await application.bot.set_my_commands([
        BotCommand("start", "Почати діалог"),
        BotCommand("stop", "Зупинити бота")
    ])

async def start(update, context):
    await update.message.reply_text("Hi, print length of password:")
    return length

async def pass_len(update, context):
    try:
        pass_len = int(update.message.text)
        password = "".join(secrets.choice(symbols) for i in range(pass_len))
        await update.message.reply_text(f"{password}")
        return length
    except:
        await update.message.reply_text("Sorry, it is not a number")
        return length

async def stop(update, context):
    await update.message.reply_text("Бот зупинено")
    return ConversationHandler.END


if __name__=="__main__":
    application = ApplicationBuilder().token("7517094807:AAHHzhZuFRnMDOLeXV_5SNYcgraCFW8SRv0").build()
    application.post_init = main

    conv_handler = ConversationHandler(
        entry_points =[CommandHandler("start", start)],
        states = {length: [MessageHandler(filters.TEXT & (~filters.COMMAND), pass_len)]},
        fallbacks = [CommandHandler("stop", stop)]
    )
    application.add_handler(conv_handler)

    application.run_polling()