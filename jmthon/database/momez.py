import threading
from . import BASE, SESSION

from sqlalchemy import Column, String
from sqlalchemy.sql.sqltypes import BigInteger



class Momez(BASE):
    __tablename__ = "momez"
    chat_id = Column(String(14), primary_key=True)
    user_id = Column(BigInteger, primary_key=True)

    def __init__(self, chat_id, user_id):
        self.chat_id = str(chat_id)
        self.user_id = user_id

    def __repr__(self):
        return "<Setmomez %s>" % self.user_id


Momez.__table__.create(checkfirst=True)

MOMEZ_INSERTION_LOCK = threading.RLock()


def setmomez(chat_id, user_id):
    with MOMEZ_INSERTION_LOCK:
        momez_user = Momez(str(chat_id), user_id)
        SESSION.add(momez_user)
        SESSION.commit()


def is_momez(chat_id, user_id):
    try:
        return SESSION.query(Momez).get((str(chat_id), user_id))
    finally:
        SESSION.close()


def delmomez(chat_id, user_id):
    with MOMEZ_INSERTION_LOCK:
        delmomez_user = SESSION.query(Momez).get((str(chat_id), user_id))
        if delmomez_user:
            SESSION.delete(delmomez_user)
            SESSION.commit()
            return True
        else:
            SESSION.close()
            return False


def list_momez(chat_id):
    try:
        return (SESSION.query(Momez).filter(
            Momez.chat_id == str(chat_id)).order_by(
                Momez.user_id.asc()).all())
    finally:
        SESSION.close()
