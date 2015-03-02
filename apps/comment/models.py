#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.model import *


class Comment(BaseModel, TimestampMixin):
    __display_name__ = 'Komentarze'

    content = Column(ForeignKey('content.id'))
    user = Column(ForeignKey('user.id'))
    text = Column(Text)
    visible = Column(Boolean, default=True)

    def __repr__(self):
        return '<Comment(id={}, user={}, content={}>'.format(self.id, self.user, self.content)