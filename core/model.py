from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


class Base(object):
    db = None

    @classmethod
    def exists(cls, *criterion):
        return bool(cls.db.query(cls).filter(*criterion).count())

    @classmethod
    def save(cls):
        cls.db.add(cls)

Base = declarative_base(cls=Base)