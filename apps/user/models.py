import hashlib
from core.model import *


class User(TimestampMixin, Base):
    name = Column(String(length=50))
    email = Column(String(length=255))
    password = Column(String(length=32))

    @before_save('password')
    def obfuscate_password(self):
        return User.hash_password(self.password)

    @staticmethod
    def hash_password(password):
        return hashlib.md5(password).hexdigest()

    def __repr__(self):
        return '<User(id={}, name={})>'.format(self.id, self.name)