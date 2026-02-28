from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import random

TOKEN = "8791724105:AAHJo9_7jrL-2eCwvp0kVHURzvSuZ3wUoaE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Йо, я Матерный Федик, блядь. Готовь жопу — щас начнётся.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "привет" in text or "здорова" in text:
        await update.message.reply_text("Привет, хуесос! Чё, опять пришёл в мою жизнь посрать?")
    elif "как дела" in text:
        await update.message.reply_text("Дела как у тебя в штанах — хуёво, но стоит.")
    elif "пошёл" in text or "нахуй" in text:
        await update.message.reply_text("Сам пошёл нахуй, мудак! Я тут король.")
    elif "сделай" in text:
        await update.message.reply_text("Сделаю, только не ной потом, когда я тебе в личку кота в жопе скину.")
    elif random.random() < 0.2:
        await update.message.reply_text("Ты сегодня дрочил или опять в мамкины трусы кончил?")
    else:
        варианты = [
            "Бля, ты меня бесишь, как будто я твой бывший.",
            "СЪЕБИСЬ, пока я не начал голосовые слать!",
            "Пиздец, ты реально это написал? Я щас обоссусь.",
            "Хочешь, я тебе в жопу вставлю... ну, в смысле, мем?",
            "Ты мне мозг выносишь, как будто я твой психотерапевт."
        ]
        await update.message.reply_text(random.choice(варианты))

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Матерный Федик запущен, блядь.")
app.run_polling()
