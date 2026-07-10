import os
from openai import OpenAI
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.environ["TOKEN"]
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Hello! I'm your AI assistant.\n\nSend me any message."
    )

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
        try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI Telegram assistant.",
                },
                {
                    "role": "user",
                    "content": user_message,
                },
            ],
        )

        await update.message.reply_text(
            response.choices[0].message.content
        )

    except Exception as e:
        await update.message.reply_text(
            f"❌ Error:\n{e}"
        app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        chat,
    )
)

print("🤖 AI Bot is running...")
app.run_polling()
