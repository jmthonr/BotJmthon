from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins

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
    if not is_admin:
        return
    if user_id == 1280124974:
        await e.reply(f"لك هلا حبيبي وتاج راسي مطوري احبك")
        return
    if is_momez(chat_id, user_id):
        await e.reply(f"المستخدم مميز بالفعل")
        return
    setmomez(chat_id, user_id)
    await e.reply(f"المستخدم تم رفعه مميز بنجاح")



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


@jmthon.on(events.ChatAction(chats=(), action=events.ChatActionTyping()))
async def set_momez_on_group_join(e):
    if e.user_added:
        chat_id = e.chat_id
        me = await jmthon.get_me()
        if me.id in e.action_message.action.users and me.id in e.action_message.action.participants:
            admin_ids = []
            async for admin in jmthon.iter_participants(chat_id, filter=ChannelParticipantsAdmins):
                admin_ids.append(admin.id)
            for admin_id in admin_ids:
                setadmin(chat_id, admin_id)
            await jmthon.send_message(chat_id, "تم رفع جميع المشرفين في رتبة الأدمن")

