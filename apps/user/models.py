import hashlib
from core.model import *


class User(TimestampMixin, Base):
    name = Column(String(length=50))
    email = Column(String(length=255))
    password = Column(String(length=32))

    @before_save('password')
    def obfuscate_password(self):
        return hashlib.md5(self.password).hexdigest()

    def __repr__(self):
        return '<User(id={}, name={})>'.format(self.id, self.name)