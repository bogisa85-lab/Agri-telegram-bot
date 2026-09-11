import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌾 Agri Signali Bot je pokrenut!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 Agri Signali Bot\n\n"
        "/start - pokretanje\n"
        "/help - pomoć"
    )


def main():
    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN nije podešen!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Agri Signali Bot je pokrenut")

    app.run_polling()


if __name__ == "__main__":
    main()