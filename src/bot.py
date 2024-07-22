#!/usr/bin/env python3
import os
import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import urllib.parse

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
FORUM_URL = os.getenv("FORUM_URL")
FORUM_URL_LOCAL = os.getenv("FORUM_URL_LOCAL")

async def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    await update.message.reply_text(f"Welcome, {user.first_name}! Please send me a keyword to search.")

def search_forum(query: str) -> str:
    encoded_query = urllib.parse.quote(query)
    search_url = f"{FORUM_URL_LOCAL}/search/999999/?q={encoded_query}&o=date"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    results = []
    for link in soup.find_all('a', href=True):
        link_text = link.text.strip()
        link_href = link['href']
        if "/threads/" in link_href:
            thread_url = f"{FORUM_URL}{link_href}"
            results.append(thread_url)

    return "\n".join(results) if results else "No results found."

async def handle_message(update: Update, context: CallbackContext) -> None:
    query = update.message.text
    search_result = search_forum(query)
    await update.message.reply_text(search_result)

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == '__main__':
    main()
