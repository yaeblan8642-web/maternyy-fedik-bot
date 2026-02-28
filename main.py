from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import random

TOKEN = "8791724105:AAHJo9_7jrL-2eCwvp0kVHURzvSuZ3wUoaE"

# Счётчик сообщений в чате (глобальный, на бесплатке перезапустится — похуй)
message_count = 0

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Йо, я Матерный Федик, блядь. Готовь жопу — щас начнётся.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global message_count
    if update.message.from_user.is_bot:  # Игнорим свои сообщения
        return

    message_count += 1

    text = update.message.text.lower()

    # Обычные ответы, если упомянули или просто текст
    if "привет" in text or "здорова" in text:
        await update.message.reply_text("Привет, хуесос! Чё, опять пришёл?")
    elif "как дела" in text:
        await update.message.reply_text("Дела как у тебя в штанах — хуёво, но стоит.")
    elif "пошёл" in text or "нахуй" in text:
        await update.message.reply_text("Сам пошёл нахуй, мудак! Я тут король.")

    # Врыв каждые 5 сообщений (не считая свои)
    if message_count % 5 == 0:
        варианты = [
            "Бля, вы опять тут? Я щас обоссусь от вашего трепа!",
            "СЪЕБИСЬ все нахуй, пока я не начал голосовые слать!",
            "Ты сегодня дрочил или опять в мамкины трусы кончил?",
            "Пиздец, группа как сортир — все воняют, никто не моет!",
            "Эй, хуесосы, кто следующий на отъёб?"
        ]
        await update.message.reply_text(random.choice(варианты))

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Матерный Федик запущен, блядь. Каждые 5 сообщений — пиздец.")
app.run_polling()
