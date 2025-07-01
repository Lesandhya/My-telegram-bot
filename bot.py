from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# /start command function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🙏 ସ୍ବାଗତ! ମୁଁ ତୁମର ସାଧାରଣ Telegram Bot।")

# Bot setup
if __name__ == '__main__':
    application = ApplicationBuilder().token("8005999110:AAHz5aDnOpMzcmSdYUilymCDIq0J95I71Tc").build()

    application.add_handler(CommandHandler("start", start))

    application.run_polling()
