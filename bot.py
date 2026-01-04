import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context):
    text = """🏆 These Are The Pros Of Joining MARCUS Community 👇

🔹Free COPY TRADING 📈 
🔹 Loss Recovery Session 💯
🔹10-15 Non Mtg Insights 🚀
🔹AI TRADE BOT FREE 🤖
🔹Daily Free 90% Working Strategy 📈
🔹5+ Years of Experience in Binary 📈
🔹Support 24/7 Assistance📱

🚀JOIN VIP GROUP LINK🔗👇

🔗 https://t.me/tradingsmarcus

🤔 Any Questions Msg Here 📥 

👉 @PoOfficial123 ✅

👇👇 TAP ON JOIN VIP NOW 👇 👇"""
    
    button = InlineKeyboardButton("🚀 JOIN VIP GROUP 💸", url="https://t.me/tradingsmarcus")
    keyboard = InlineKeyboardMarkup([[button]])
    
    await update.message.reply_photo(
        photo="https://i.postimg.cc/sx3sryfQ/IMG-20260104-095102-116.jpg",
        caption=text,
        reply_markup=keyboard
    )

def main():
    if not TOKEN:
        print("❌ ERROR: BOT_TOKEN not set!")
        return
    
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("promo", start))
    
    print("✅ Bot running on Koyeb!")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
