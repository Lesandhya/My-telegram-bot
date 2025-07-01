from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# /start command function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📢 Join Our Channel", url="https://t.me/+2CwhuwoujTNiNGU0")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🙏 ଧନ୍ୟବାଦ! ଆପଣ ଆମ Telegram Bot ରେ ସ୍ୱାଗତ।",
        reply_markup=reply_markup
    )

# Bot setup
if __name__ == "__main__":
    application = ApplicationBuilder().token("8005999110:AAHz5aDnOpMzcmSdYUilymCDIq0J95I71Tc").build()

    application.add_handler(CommandHandler("start", start))
    application.run_polling()
