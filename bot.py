from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "YOUR_BOT_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Hello! My bot is online.")

app = Application.builder().token(8827990357:AAHnBkVm0pevpoVDIXDuHXfLCN7RhiJNzSg).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
