from telethon import TelegramClient
import logging
import sys
from config import APP_ID, API_HASH, TOKEN

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.INFO
)


jmthon = TelegramClient("jmthon-bot", APP_ID, API_HASH)

try:
    jmthon.start(bot_token=TOKEN)
except Exception:
    print("Bot Token Invalid - التوكن غير صحيح")
    sys.exit(1)
