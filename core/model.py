from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound


# Decorator that adds callback to model's field to execute before save (it value modified).
# Example:
#     @before_save('password')
#     def hash_password(password):
#         return some_hashing_function(password)
def before_save(field_name):
    def wrapper(before_field_save_function):
        before_field_save_function.run_before_save = field_name
        return before_field_save_function

    return wrapper


class TimestampMixin(object):
    created_at = Column(DateTime, default=func.now())


class SQLExtensions(object):
    @classmethod
    def query(cls):
        return cls.db_session.query(cls)

    @classmethod
    def get(cls, *criterion):
        return cls.db_session.query(cls).filter(*criterion).one()

    @classmethod
    def exists(cls, *criterion):
        return bool(cls.db_session.query(cls).filter(*criterion).count())

    def save(self):
        # Search for model's fields callbacks that should be executed before save,
        # BUT only when field value has changed.
        for method_name in dir(self):
            method = getattr(self, method_name)

            if hasattr(method, 'run_before_save'):
                field_to_modify = getattr(method, 'run_before_save')

                if field_to_modify in self.__dict__['_sa_instance_state'].committed_state:
                    setattr(self, field_to_modify, method())

        BaseModel.db_session.add(self)
        BaseModel.db_session.commit()

        return self


class BaseModel(SQLExtensions):
    db_session = None

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    @declared_attr
    def display_name(cls):
        return getattr(cls, '__display_name__', cls.__tablename__)

    @classmethod
    def fields(cls):
        return cls.metadata.tables[cls.__tablename__].columns

    id = Column(Integer, primary_key=True)


BaseModel = declarative_base(cls=BaseModel)