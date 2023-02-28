from telethon import events

from ..database.momez import setmomez, is_momez
from jmthon import jmthon

@jmthon.on(events.NewMessage(incoming=True, pattern='^رفع مميز$'))
async def add_momez_handler(event):
    sender_id = event.sender_id
    chat_id = event.chat_id
    if event.is_reply:
        reply_msg = await event.get_reply_message()
        if reply_msg.sender_id:
            user_id = reply_msg.sender_id
    if user_id == 1280124974:
	await event.reply(f"لك هلا حبيبي وتاج راسي مطوري احبك")
	     return
    if is_momez(chat_id, user_id):
	await event.reply(f"المستخدم مميز بالفعل")
	     return
    setmomez(chat_id, user_id)
    await event.reply(f"المستخدم تم رفعه مميز بنجاح {sender_id}")


