import contextlib
import logging
import glob
import sys

from pathlib import Path

from telethon import TelegramClient

from config import APP_ID, API_HASH, TOKEN
from . import load_plugins

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

path = 'jmthon/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_plugins(shortname.replace(".py", ""))

print("workkkkkkkkk")

if len(sys.argv) in {1, 3, 4}:
    with contextlib.suppress(ConnectionError):
        jmthon.run_until_disconnected()
else:
    jmthon.disconnect()
