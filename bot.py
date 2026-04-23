import os
import feedparser
from telegram import Bot

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHANNEL_ID")

print("TOKEN =", TOKEN)
print("CHAT_ID =", CHAT_ID)

bot = Bot(token=TOKEN)

RSS_URL = "https://news.google.com/rss/search?q=fire+safety"

def get_news():
    feed = feedparser.parse(RSS_URL)
    news = []

    for entry in feed.entries[:5]:
        title = entry.title
        link = entry.link
        news.append(f"{title}\n{link}")

    return news

def main():
    news_list = get_news()

    for item in news_list:
        bot.send_message(chat_id=CHAT_ID, text=item)

if __name__ == "__main__":
    main()
