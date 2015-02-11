#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.model import *


class Category(Base, TimestampMixin):
    __display_name__ = 'Kategorie'

    name = Column(String(length=255))
    parent = Column(Integer, ForeignKey('category.id'))
    
    def __repr__(self):
        return '<Category(id={})>'.format(self.id)