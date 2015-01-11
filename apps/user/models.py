import hashlib
from sqlalchemy.orm import validates
from core.model import *


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=30))
    password = Column(String(length=32))

    @validates('name')
    def validate_name(self, key, name):
        assert name != '', 'Please specify user name.'
        assert 3 <= len(name) <= 30, 'Name must be 3-30 characters long.'
        assert not self.exists(User.id != self.id, User.name == name), 'This user name is taken.'

        return name

    @validates('password')
    def validate_password(self, key, password):
        return hashlib.md5(password).hexdigest()

    def __repr__(self):
        return '<User(id={}, name={})>'.format(self.id, self.name)