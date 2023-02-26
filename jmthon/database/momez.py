try:
    from . import BASE, SESSION
except ImportError as e:
    raise Exception("Hello!") from e
from sqlalchemy import Column, String


class Momez(BASE):
    __tablename__ = "momez"
    sender_id = Column(String(14), primary_key=True)
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, sender_id, chat_id):
        self.sender_id = str(sender_id)
        self.chat_id = str(chat_id)

def add_momez(sender_id, chat_id):
    momez = Momez(str(sender_id), str(chat_id))
    SESSION.add(momez)
    SESSION.commit()

    
def del_momez(sender_id, chat_id):
    if momez := SESSION.query(Momez).get((str(sender_id), str(chat_id))):
        SESSION.delete(momez)
        SESSION.commit()


def get_momez_list():
    momezes = SESSION.query(Momez).all()
    SESSION.close()
    return [(momez.sender_id, momez.chat_id) for momez in momezes]
