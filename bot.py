import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

IMAGE_URL = "https://i.postimg.cc/sx3sryfQ/IMG-20260104-095102-116.jpg"

CAPTION = """🏆 These Are The Pros Of Joining MARCUS Community 👇

🔹 Free COPY TRADING 📈
🔹 Loss Recovery Session 💯
🔹 10–15 Non MTG Insights 🚀
🔹 AI TRADE BOT FREE 🤖
🔹 Daily Free 90% Working Strategy 📈
🔹 5+ Years of Experience in Binary 📈
🔹 Support 24/7 Assistance 📱

🤔 Any Questions? Msg Here 👇
👉 @PoOfficial123 ✅

👇👇 TAP ON JOIN VIP NOW 👇👇
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 JOIN VIP GROUP 💸", url="https://t.me/tradingsmarcus")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo=IMAGE_URL,
        caption=CAPTION,
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
