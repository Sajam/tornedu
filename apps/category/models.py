from core.model import *


class Category(Base, TimestampMixin):
    def __repr__(self):
        return '<Category(id={})>'.format(self.id)