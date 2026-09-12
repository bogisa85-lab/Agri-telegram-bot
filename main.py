Pošto još nemamo potvrđen izvor stvarnih cena, **nemoj sada lepiti kod koji tvrdi da daje live CBOT cene**. Završićemo sa istom greškom kao malopre.

Umesto toga, evo **kompletnog `main.py`** koji radi kao Agri Signal bot, sa komandama za pšenicu, kukuruz, soju, signale i izveštaj. Kasnije samo zamenimo funkciju koja vraća podatke kada pronađemo stabilan izvor cena.

**Obriši ceo `main.py` i nalepi ovo:**

```python
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌾 AGRI SIGNALI BOT\n\n"
        "Komande:\n"
        "/wheat - Pšenica\n"
        "/corn - Kukuruz\n"
        "/soybeans - Soja\n"
        "/signals - Signali\n"
        "/report - Dnevni izveštaj\n"
        "/help - Pomoć"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)


async def wheat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌾 PŠENICA\n\n"
        "Cena: podaci nisu povezani\n"
        "Trend: ČEKA SE PODATAK\n"
        "Signal: ČEKA SE ANALIZA"
    )


async def corn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌽 KUKURUZ\n\n"
        "Cena: podaci nisu povezani\n"
        "Trend: ČEKA SE PODATAK\n"
        "Signal: ČEKA SE ANALIZA"
    )


async def soybeans(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🫘 SOJA\n\n"
        "Cena: podaci nisu povezani\n"
        "Trend: ČEKA SE PODATAK\n"
        "Signal: ČEKA SE ANALIZA"
    )


async def signals(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 AGRI SIGNALI\n\n"
        "🌾 Wheat: ČEKA SE ANALIZA\n"
        "🌽 Corn: ČEKA SE ANALIZA\n"
        "🫘 Soybeans: ČEKA SE ANALIZA"
    )


async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 DNEVNI AGRI IZVEŠTAJ\n\n"
        "🌾 Wheat: podaci nisu povezani\n"
        "🌽 Corn: podaci nisu povezani\n"
        "🫘 Soybeans: podaci nisu povezani\n\n"
        "Automatska analiza biće dodata nakon povezivanja tržišnih podataka."
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
    app.add_handler(CommandHandler("report", report))

    print("Agri Signali Bot je pokrenut")

    app.run_polling()


if __name__ == "__main__":
    main()