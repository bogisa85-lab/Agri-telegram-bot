import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌾 AGRI SIGNALI BOT\n\n"
        "Dostupne komande:\n"
        "/wheat - pšenica\n"
        "/corn - kukuruz\n"
        "/soybeans - soja\n"
        "/signals - agrarni signali\n"
        "/news - agrarne vesti\n"
        "/report - dnevni izveštaj"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌾 AGRI SIGNALI BOT\n\n"
        "/wheat - pšenica\n"
        "/corn - kukuruz\n"
        "/soybeans - soja\n"
        "/signals - signali\n"
        "/news - vesti\n"
        "/report - izveštaj"
    )


async def wheat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌾 PŠENICA\n\n"
        "CBOT: priprema podataka...\n"
        "Trend: čeka se tržišni podatak\n"
        "Signal: čeka se analiza\n\n"
        "⚠️ Cena još nije prikazana jer bot "
        "još nije povezan sa stvarnim tržišnim izvorom."
    )


async def corn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌽 KUKURUZ\n\n"
        "Tržišni podaci se pripremaju."
    )


async def soybeans(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🫘 SOJA\n\n"
        "Tržišni podaci se pripremaju."
    )


async def signals(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 AGRI SIGNALI\n\n"
        "Signali će biti aktivirani nakon povezivanja "
        "sa stvarnim tržišnim podacima."
    )


async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📰 AGRARNE VESTI\n\n"
        "Izvor vesti još nije povezan."
    )


async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 DNEVNI AGRI IZVEŠTAJ\n\n"
        "Izveštaj će biti aktiviran nakon povezivanja "
        "tržišnih podataka i vesti."
    )


def main():
    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN nije podešen!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("wheat", wheat))
    app.add_handler(CommandHandler("corn", corn))
    app.add_handler(CommandHandler("soybeans", soybeans))
    app.add_handler(CommandHandler("signals", signals))
    app.add_handler(CommandHandler("news", news))
    app.add_handler(CommandHandler("report", report))

    print("Agri Signali Bot je pokrenut")

    app.run_polling()


if __name__ == "__main__":
    main()