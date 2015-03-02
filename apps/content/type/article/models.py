#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.model import *
from ...models import Content


class Article(Content):
    __display_name__ = 'Artykuł'

    id = Column(Integer, ForeignKey('content.id'), primary_key=True)
    content = Column(UnicodeText)

    __mapper_args__ = {
        'polymorphic_identity': 'article',
    }

    def __repr__(self):
        return '<Article(id={}, name={})>'.format(self.id, self.name)