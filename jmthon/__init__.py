import contextlib
import logging
import sys

from telethon import TelegramClient

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


if len(sys.argv) in {1, 3, 4}:
    with contextlib.suppress(ConnectionError):
        jmthon.run_until_disconnected()
else:
    jmthon.disconnect()
