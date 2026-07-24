from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привіт! Я бот для відстеження розмірів Zara.\n\n"
        "Надішли мені посилання на товар."
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "zara.com" in text:
        context.user_data["url"] = text
        await update.message.reply_text(
            "✅ Посилання отримано.\nТепер напиши потрібний розмір (наприклад: S, M, L або 40)."
        )
    else:
        await update.message.reply_text(
            f"📏 Добре! Потрібний розмір: {text}\n\n"
            "🚧 Перевірку Zara ми додамо на наступному кроці."
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    app.run_polling()

if __name__ == "__main__":
    main()
