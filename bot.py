import logging, os
import random
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler

def load_dotenv(path = ".env"):
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value


load_dotenv()


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
    TOKEN = os.environ.get("TELEGRAM_TOKEN")
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    answers_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), reply)
    application.add_handler(answers_handler)

    application.run_polling()