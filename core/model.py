from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, Integer, String, DateTime, func


class SQLExtensions(object):
    @classmethod
    def get(cls, *criterion):
        return cls.db.query(cls).filter(*criterion).one()

    @classmethod
    def exists(cls, *criterion):
        return bool(cls.db.query(cls).filter(*criterion).count())

    def save(self):
        for method_name in dir(self):
            method = getattr(self, method_name)
            if hasattr(method, 'run_before_save'):
                field_to_modify = getattr(method, 'run_before_save')

                if field_to_modify in self.__dict__['_sa_instance_state'].committed_state:
                    setattr(self, field_to_modify, method())

        Base.db.add(self)


class TimestampMixin(object):
    created_at = Column(DateTime, default=func.now())


class Base(SQLExtensions):
    db = None

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


def before_save(field_name):
    def wrapper(before_field_save_function):
        before_field_save_function.run_before_save = field_name
        return before_field_save_function

    return wrapper


Base = declarative_base(cls=Base)