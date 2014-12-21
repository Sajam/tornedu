from core.model import *


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=30))
    password = Column(String(length=32))

    def __repr__(self):
        return '<User(id={}, name={})>'.format(self.id, self.name)