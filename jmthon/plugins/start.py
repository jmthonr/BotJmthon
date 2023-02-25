from telethon import events, Button
from jmthon import jmthon

@jmthon.on(events.NewMessage(incoming=True, pattern='/start'))
async def _startmsg(event):
    text = f"Hi {get_mention(event)}, I Am Alive."
    await event.reply(text, buttons=[
    [Button.url('⭐ Dev ⭐', 'https://t.me/jmthon')],
    [Button.url('❤ Join Channel ❤', 'https://t.me/R0R77')]
])
    return
