from telethon import events, Button
from .. import jmthon
from . import get_mention

@jmthon.on(events.NewMessage(incoming=True, pattern='/start'))
async def _startmsg(e):
    if not e.is_private:
        return
    text = f"Hi {get_mention(e)}, I Am Alive."
    await e.reply(text, buttons=[
    [Button.url('⭐ Dev ⭐', 'https://t.me/jmthon')],
    [Button.url('❤ Join Channel ❤', 'https://t.me/R0R77')]
])
    return
