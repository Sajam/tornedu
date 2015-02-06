#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.model import *


class Category(Base, TimestampMixin):
    __display_name__ = 'Kategorie'
    
    def __repr__(self):
        return '<Category(id={})>'.format(self.id)