import logging
import random
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

answers = [
    "Так ✅",
    "Ні ❌",
    "Можливо 🤔",
    "Скоро дізнаєшся ⏳",
    "Не розраховуй на це 🚫",
    "Однозначно так! 🎉",
    "Дуже сумнівно 🤨"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Привіт! Я магічна куля 🎱. Задай мені питання!")

async def reply(update, context):
    response = random.choice(answers)
    await update.message.reply_text(response)

if __name__ == '__main__':
    application = ApplicationBuilder().token('7608067984:AAGf7bwsifedaDlNJjJM8XTyCMmiFFLaLvU').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    answers_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), reply)
    application.add_handler(answers_handler)

    application.run_polling()