#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.model import *
from ...models import Content
from .providers import VideoProvider


class Video(Content):
    id = Column(Integer, ForeignKey('content.id'), primary_key=True)
    provider = Column(Enum(*VideoProvider.get_types().keys()))
    content = Column(String(length=500))
    duration = Column(Interval)

    __mapper_args__ = {
        'polymorphic_identity': 'video',
    }

    def __repr__(self):
        return '<Video(id={}, name={})>'.format(self.id, self.name)