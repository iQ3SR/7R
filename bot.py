import os
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
AI_URL = os.getenv("AI_SERVER_URL")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    # إرسال الطلب للسيرفر
    response = requests.post(AI_URL, json={"prompt": user_text})
    data = response.json()

    ai_reply = data.get("response", "حدث خطأ في السيرفر.")

    await update.message.reply_text(ai_reply)

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("BOT IS RUNNING...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
