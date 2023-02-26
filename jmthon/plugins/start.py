from telethon import events, Button
from ..database.globals import set, get
from .. import jmthon
from . import get_mention

@jmthon.on(events.NewMessage(incoming=True, pattern='/start'))
async def _startmsg(e):
    if not e.is_private:
        return
    text = f"ها {get_mention(e)}"
    await e.reply(text, buttons=[
    [Button.url('السورس', 'https://t.me/jmthon')],
    [Button.url('المطور', 'https://t.me/R0R77')]
])
    return

@jmthon.on(events.NewMessage(incoming=True, pattern='^بوت$'))
async def enable_group(e):
    if e.is_private:
        return
    await e.reply("كس امك مو بوت اسمي سينكو")

@jmthon.on(events.NewMessage(incoming=True, pattern='^سينكو$'))
async def enable_group(e):
    if e.is_private:
        return
    await e.reply("تفضل شنو تريد من سينكو")
