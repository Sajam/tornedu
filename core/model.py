from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, Integer, String, DateTime, func


class SQLExtensions(object):
    @classmethod
    def exists(cls, *criterion):
        return bool(cls.db.query(cls).filter(*criterion).count())

    def save(self):
        Base.db.add(self)


class TimestampMixin(object):
    created_at = Column(DateTime, default=func.now())


class Base(SQLExtensions):
    db = None

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)