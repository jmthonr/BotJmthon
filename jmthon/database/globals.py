try:
    from . import BASE, SESSION
except ImportError as e:
    raise AttributeError from e
from sqlalchemy import Column, String, UnicodeText


class Globals(BASE):
    __tablename__ = "globals"
    variable = Column(String, primary_key=True, nullable=False)
    value = Column(UnicodeText, primary_key=True, nullable=False)

    def __init__(self, variable, value):
        self.variable = str(variable)
        self.value = value


Globals.__table__.create(checkfirst=True)


def get(variable):
    try:
        return (
            SESSION.query(Globals)
            .filter(Globals.variable == str(variable))
            .first()
            .value
        )
    except BaseException:
        return None
    finally:
        SESSION.close()


def set(variable, value):
    if SESSION.query(Globals).filter(Globals.variable == str(variable)).one_or_none():
        deldb(variable)
    adder = Globals(str(variable), value)
    SESSION.add(adder)
    SESSION.commit()


def deldb(variable):
    if rem := (
        SESSION.query(Globals)
        .filter(Globals.variable == str(variable))
        .delete(synchronize_session="fetch")
    ):
        SESSION.commit()
        SESSION.commit()
