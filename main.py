import os
import httpx
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌾 AGRI SIGNALI BOT\n\n"
        "/wheat - pšenica\n"
        "/help - pomoć"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌾 AGRI SIGNALI BOT\n\n"
        "/wheat - pšenica"
    )

async def wheat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        url = "https://api.agsist.com/quotes"
        async with httpx.AsyncClient(timeout=15) as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()

        await update.message.reply_text(
            f"🌾 PŠENICA\n\n"
            f"Podaci sa tržišta:\n{data}"
        )

    except Exception as e:
        await update.message.reply_text(
            "⚠️ Trenutno ne mogu da preuzmem tržišne podatke.\n"
            "Pokušaj ponovo za nekoliko minuta."
        )
        print(f"Wheat error: {e}")

def main():
    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN nije podešen!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("wheat", wheat))

    print("Agri Signali Bot je pokrenut")
    app.run_polling()

if __name__ == "__main__":
    main()