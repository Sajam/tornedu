#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from core.model import *
from ...models import Content
from .providers import VideoProvider


class Video(Content):
    __display_name__ = 'Wideo'

    id = Column(Integer, ForeignKey('content.id'), primary_key=True)
    provider = Column(Enum(*VideoProvider.get_types().keys()))
    content = Column(String(length=500))
    duration = Column(Interval, nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'video',
    }

    @before_save('duration')
    def duration_as_timedelta(self):
        if self.duration and self.duration != '00:00:00':
            return datetime.timedelta(
                **dict(zip(
                    ['hours', 'minutes', 'seconds'],
                    map(lambda v: int(v), self.duration.split(':'))
                ))
            )

    def __repr__(self):
        return '<Video(id={}, name={})>'.format(self.id, self.name)