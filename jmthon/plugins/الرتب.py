from telethon import events

from ..database.momez import add_momez 
from jmthon import jmthon

@jmthon.on(events.NewMessage(incoming=True, pattern='^رفع مميز$'))
async def add_momez_handler(event):
    sender_id = event.sender_id
    chat_id = event.chat_id
    if event.is_reply:
        reply_msg = await event.get_reply_message()
        if reply_msg.sender_id:
            sender_id = reply_msg.sender_id
    add_momez(sender_id, chat_id)
    await event.respond(f"المستخدم تم رفعه مميز بنجاح {sender_id}")
