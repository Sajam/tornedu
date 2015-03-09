#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.model import *


class ContentHistory(BaseModel, TimestampMixin):
    __display_name__ = 'Historia oglądanych treści'

    user = Column(ForeignKey('user.id'))
    content = Column(ForeignKey('content.id'))

    def __repr__(self):
        return '<ContentHistory(id={}, user={}, content={})>'.format(self.id, self.user, self.content)


class ContentBookmarks(BaseModel, TimestampMixin):
    __display_name__ = 'Zapisane treści'

    user = Column(ForeignKey('user.id'))
    content = Column(ForeignKey('user.id'))

    def __repr__(self):
        return '<ContentBookmarks(id={}, user={}, content={})>'.format(self.id, self.user, self.content)


class FollowedCategory(BaseModel, TimestampMixin):
    __display_name__ = 'Obserwowane kategorie'

    user = Column(ForeignKey('user.id'))
    category = Column(ForeignKey('category.id'))
    last_checked = Column(DateTime, nullable=True)
    notify = Column(Enum('web', 'email'), default='email')
    count = Column(Integer, default=0)

    def __repr__(self):
        return '<FollowedCategory(id={}, user={}, category={})>'.format(self.id, self.user, self.category)


class FollowedContent(BaseModel, TimestampMixin):
    __display_name__ = 'Obserwowane treści'

    user = Column(ForeignKey('user.id'))
    content = Column(ForeignKey('content.id'))
    reason = Column(Enum('comment', 'button'), default='comment')

    def __repr__(self):
        return '<FollowedContent(id={}, user={}, content={})>'.format(self.id, self.user, self.content)