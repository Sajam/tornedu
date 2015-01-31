# import hashlib
from core.model import *


class User(TimestampMixin, Base):
    name = Column(String(length=50))
    email = Column(String(length=255))
    password = Column(String(length=32))

    # hashlib.md5(password).hexdigest()

    def __repr__(self):
        return '<User(id={}, name={})>'.format(self.id, self.name)