#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import OrderedDict
from core.model import *


class Category(BaseModel, TimestampMixin):
    __display_name__ = 'Kategorie'

    name = Column(String(length=255))
    parent = Column(Integer, ForeignKey('category.id', ondelete='CASCADE'))

    @staticmethod
    def items(*args, **kwargs):
        result = []
        categories = Category.filter(Category.parent == kwargs['parent']).all()\
            if 'parent' in kwargs else filter(lambda c: not c.parent, Category.all())

        def sort_and_set_levels(items, level=0, insert_at_index=-1):
            for category in items:
                insert_at_index += 1
                category.level = level

                result.insert(insert_at_index, category)

                insert_at_index = sort_and_set_levels(filter(lambda c: c.parent == category.id, categories),
                                                      level=level + 1, insert_at_index=insert_at_index)
            return insert_at_index

        sort_and_set_levels(categories)

        return filter(lambda c: c.level == kwargs['level'], result) if 'level' in kwargs else result

    @staticmethod
    def tree_select_options(level_indicator=None, **kwargs):
        blank = kwargs.get('blank', False)
        level_indicator = level_indicator or '&nbsp;' * 4
        options = [(category.id, '{} {}'.format(level_indicator * category.level, category.name))
                   for category in Category.items()]

        if blank:
            options = [('', '--- wybierz ---')] + options

        return OrderedDict(options)

    def __repr__(self):
        return '<Category(id={}, name={})>'.format(self.id, self.name)