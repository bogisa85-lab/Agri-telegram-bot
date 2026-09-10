Odlično. 🌾 Sad imamo osnovu. Sledeće ćemo napraviti da bot **odgovara na Telegram poruke**, a tek onda dodajemo tržišne podatke, signale i izveštaje.

### Korak 3 — ubaci kod u `main.py`

1. Otvori **`main.py`**.
2. Klikni **Edit**.
3. U prazno polje kopiraj **ceo ovaj kod**:

```python
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌾 AGri Signali Bot\n\n"
        "Bot je pokrenut!\n\n"
        "Za sada mogu da koristim:\n"
        "/start - početak\n"
        "/help - pomoć\n"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 AGri Signali Bot\n\n"
        "Uskoro dodajemo:\n"
        "🌾 Pšenicu\n"
        "🌽 Kukuruz\n"
        "🫘 Soju\n"
        "🌱 Uljanu repicu\n"
        "🌻 Suncokret\n\n"
        "📈 Tehničke signale\n"
        "📰 USDA i tržišne vesti\n"
        "🌦️ Vremenske uticaje\n"
        "📋 Dnevne izveštaje"
    )


def main():
    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN nije podešen!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Agri Signali Bot je pokrenut...")
    app.run_polling()


if __name__ == "__main__":
    main()
