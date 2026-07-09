import os

import re

from telegram import Update

from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(

        "🤖 Hello!\n\nUse:\n/checknumber +919876543210"

    )

async def checknumber(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:

        await update.message.reply_text(

            "Usage:\n/checknumber +919876543210"

        )

        return

    number = context.args[0]

    if re.fullmatch(r"\+[1-9]\d{7,14}", number):

        await update.message.reply_text(f"✅ Valid phone number:\n{number}")

    else:

        await update.message.reply_text("❌ Invalid phone number.")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(CommandHandler("checknumber", checknumber))

app.run_polling()
