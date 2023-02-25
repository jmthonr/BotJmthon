from telethon import events 

def get_mention(event):
    return "["+event.message.sender.first_name+"](tg://user?id="+str(event.message.sender.id)+")"
