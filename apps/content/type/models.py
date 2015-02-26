#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from core.conf import Settings
from core.utils import directories_in_path, import_class_from_path
from core.model import *


class Content(BaseModel, TimestampMixin):
    __display_name__ = 'Treści'

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


for type in directories_in_path(os.path.join(Settings.BASE_PATH, 'apps/content/type')):
    import_class_from_path('models', 'apps.content.type.{}'.format(type))