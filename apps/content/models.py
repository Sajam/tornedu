#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.model import *
from core.conf import Settings
from core.utils import import_subclasses


class Content(BaseModel, TimestampMixin):
    __display_name__ = 'Treść'

    type = Column(String(length=255))
    user = Column(ForeignKey('user.id'))
    category = Column(ForeignKey('category.id'))
    name = Column(String(length=255))
    views = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'content',
        'polymorphic_on': type,
        'with_polymorphic': '*'
    }

    def __repr__(self):
        return '<Content(id={}, name={})>'.format(self.id, self.name)


content_types = import_subclasses(Content, allowed_paths=['apps.content.type.*.models'], base_path=Settings.BASE_PATH)
content_types = {content_type.__mapper_args__['polymorphic_identity']: content_type.__display_name__
                 for content_type in content_types}