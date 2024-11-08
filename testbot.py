import logging
import os 
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    ChatMemberHandler,
    ContextTypes,
)


class TelegramBot:
    def __init__(self, token: str):
        # Initialize the bot with the BOT Token
        self.token = token
        self.app = Application.builder().token(self.token).build()

        # Set up logging to record to terminal
        logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

    # Define a function to handle new chat members
    async def greet_new_member(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        logging.info("New chat member detected")
        logging.info(update.chat_member.new_chat_member)
        new_member = update.chat_member.new_chat_member
        if new_member.user.is_bot:
            return
        
        # Edge case: If member leave the group, don't greet
        if new_member.status == "left":
            return
        
            # Send a greeting message to the new member
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Welcome, {new_member.user.full_name}!", 
            parse_mode='HTML'
        )

    def start(self):
        # Add a handler to greet new chat members
        self.app.add_handler(ChatMemberHandler(self.greet_new_member, ChatMemberHandler.CHAT_MEMBER))

        # Start the bot
        self.app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv("API_TOKEN")
    if TOKEN is None:
        raise ValueError("API_TOKEN must be set in .env file")
    bot = TelegramBot(TOKEN)
    bot.start()