import threading
from . import BASE, SESSION

from sqlalchemy import Column, String
from sqlalchemy.sql.sqltypes import BigInteger



class Admin(BASE):
    __tablename__ = "admin"
    chat_id = Column(String(14), primary_key=True)
    user_id = Column(BigInteger, primary_key=True)

    def __init__(self, chat_id, user_id):
        self.chat_id = str(chat_id)
        self.user_id = user_id

    def __repr__(self):
        return "<Setadmin %s>" % self.user_id


Admin.__table__.create(checkfirst=True)

ADMIN_INSERTION_LOCK = threading.RLock()


def setadmin(chat_id, user_id):
    with ADMIN_INSERTION_LOCK:
        admin_user = Admin(str(chat_id), user_id)
        SESSION.add(admin_user)
        SESSION.commit()


def is_admin(chat_id, user_id):
    try:
        return SESSION.query(Admin).get((str(chat_id), user_id))
    finally:
        SESSION.close()


def deladmin(chat_id, user_id):
    with ADMIN_INSERTION_LOCK:
        deladmin_user = SESSION.query(Admin).get((str(chat_id), user_id))
        if deladmin_user:
            SESSION.delete(deladmin_user)
            SESSION.commit()
            return True
        else:
            SESSION.close()
            return False


def list_admin(chat_id):
    try:
        return (SESSION.query(Admin).filter(
            Admin.chat_id == str(chat_id)).order_by(
                Admin.user_id.asc()).all())
    finally:
        SESSION.close()
