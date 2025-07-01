from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)

# 👉 Owner ID for broadcast (only this user can use /all)
OWNER_ID = 7634652648

# /start command function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📢 Join Our Channel", url="https://t.me/+2CwhuwoujTNiNGU0")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🙏 ଧନ୍ୟବାଦ! ଆପଣ ଆମ Telegram Bot ରେ ଆସିଛନ୍ତି।",
        reply_markup=reply_markup
    )

# /all command for broadcast (owner only)
async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("❌ ଆପଣଙ୍କୁ ଏହି ଆଦେଶ ଦେବା ଅନୁମତି ନାହିଁ।")
        return

    message = ' '.join(context.args)
    if not message:
        await update.message.reply_text("ℹ️ ବ୍ରୋଡ୍‌କାଷ୍ଟ ପାଇଁ କିଛି ମେସେଜ୍ ଦିଅନ୍ତୁ।\nଉଦାହରଣ: `/all Hello friends!`", parse_mode="Markdown")
        return

    # Get all chats the bot has seen so far
    for user_id in context.application.chat_data.keys():
        try:
            await context.bot.send_message(chat_id=user_id, text=message)
        except Exception as e:
            print(f"Failed to send message to {user_id}: {e}")

    await update.message.reply_text("✅ ବ୍ରୋଡକାଷ୍ଟ ସଫଳ ହେଲା!")

# Save user ID when they send any message
async def save_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.application.chat_data[update.effective_chat.id] = {}

# Main bot setup
if __name__ == "__main__":
    application = ApplicationBuilder().token("8005999110:AAHz5aDnOpMzGnsd0VlJymcIDqJ9s1jPTTc").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("all", broadcast))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, save_user))

    application.run_polling()
