from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from ..utils.utils import *
from ..database.admin import setadmin, is_admin, deladmin
from ..database.momez import setmomez, is_momez, delmomez
from jmthon import jmthon

@jmthon.on(events.NewMessage(incoming=True, pattern='^رفع مميز$'))
async def add_momez(e):
    if e.is_private:
        return
    sender_id = e.sender_id
    chat_id = e.chat_id
    if e.is_reply:
        reply_msg = await e.get_reply_message()
        if reply_msg.sender_id:
            user_id = reply_msg.sender_id
    user = await get_user_from_event(e)
    if not user:
        return
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    if not is_admin:
        return
    if user_id == 1280124974:
        await e.reply(f"لك هلا حبيبي وتاج راسي مطوري احبك")
        return
    if is_momez(chat_id, user_id):
        await e.reply(f"المستخدم مميز بالفعل")
        return
    setmomez(chat_id, user_id)
    await e.reply(f"المستخدم [{tag}](tg://user?id={user.id}) \n- تم رفعه مميز")

@jmthon.on(events.NewMessage(incoming=True, pattern='^تنزيل مميز$'))
async def add_momez(e):
    if e.is_private:
        return
    sender_id = e.sender_id
    chat_id = e.chat_id
    if e.is_reply:
        reply_msg = await e.get_reply_message()
        if reply_msg.sender_id:
            user_id = reply_msg.sender_id
    if not is_admin:
        return
    if user_id == 1280124974:
        await e.reply(f"لك هلا حبيبي وتاج راسي مطوري احبك")
        return
    if not is_momez(chat_id, user_id):
        await e.reply(f"المستخدم غير مميز اصلا")
        return
    delmomez(chat_id, user_id)
    await e.reply(f"المستخدم تم تنزيله من رتبة المميز بنجاح")



@jmthon.on(events.NewMessage(incoming=True, pattern='^رفع ادمن$'))
async def add_momez(e):
    if e.is_private:
        return
    sender_id = e.sender_id
    chat_id = e.chat_id
    if e.is_reply:
        reply_msg = await e.get_reply_message()
        if reply_msg.sender_id:
            user_id = reply_msg.sender_id
    #if not is_admin:
      #  return
    if user_id == 1280124974:
        await e.reply(f"لك هلا حبيبي وتاج راسي مطوري احبك")
        return
    if is_admin(chat_id, user_id):
        await e.reply(f"المستخدم ادمن بالفعل")
        return
    setadmin(chat_id, user_id)
    await e.reply(f"المستخدم تم رفعه ادمن بنجاح")




@jmthon.on(events.NewMessage(incoming=True, pattern='^تنزيل ادمن$'))
async def add_momez(e):
    if e.is_private:
        return
    sender_id = e.sender_id
    chat_id = e.chat_id
    if e.is_reply:
        reply_msg = await e.get_reply_message()
        if reply_msg.sender_id:
            user_id = reply_msg.sender_id
    #if not is_admin:
      #  return
    if user_id == 1280124974:
        await e.reply(f"لك هلا حبيبي وتاج راسي مطوري احبك")
        return
    if not is_admin(chat_id, user_id):
        await e.reply(f"المستخدم غير ادمن اصلا")
        return
    deladmin(chat_id, user_id)
    await e.reply(f"المستخدم تم تنزيله من رتبة الادمن بنجاح")


@jmthon.on(events.NewMessage(incoming=True, pattern='^رفع مالك$'))
async def add_momez(e):
    if e.is_private:
        return
    sender_id = e.sender_id
    chat_id = e.chat_id
    if e.is_reply:
        reply_msg = await e.get_reply_message()
        if reply_msg.sender_id:
            user_id = reply_msg.sender_id
    if not is_malk:
        return
    if user_id == 1280124974:
        await e.reply(f"لك هلا حبيبي وتاج راسي مطوري احبك")
        return
    if is_malk(chat_id, user_id):
        await e.reply(f"المستخدم ادمن بالفعل")
        return
    setmalk(chat_id, user_id)
    await e.reply(f"المستخدم تم رفعه ادمن بنجاح")
