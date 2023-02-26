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


@jmthon.on(events.NewMessage(incoming=True, pattern='^تفعيل'))
async def enable_group(event):
    chat_id = event.chat_id
    if get("TF3EL"):
        await event.reply("ألمجموعة مفعلة بنجاح")
    else:
        set("TF3EL", "Done")
        await event.reply("تم بنجاح تفعيل المجموعة بنجاح")


@jmthon.on(events.NewMessage(incoming=True, pattern='^سينكو'))
async def enable_group(event):
    await event.reply("اسمي مو سينكو كسخت صادق")
