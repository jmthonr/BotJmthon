from telethon import events, Button
from ..database.globals import add, get
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



@jmthon.on(events.NewMessage(incoming=True, pattern='^تفعيل'))
async def enable_group(event):
    chat_id = event.chat_id
    if get("TF3EL"):
        await event.reply("ألمجموعة مفعلة بنجاح")
    else:
        add("TF3EL", "Done")
        await event.reply("تم بنجاح تفعيل المجموعة بنجاح")
