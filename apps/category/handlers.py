#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.web import RequestHandler, ajax
from .models import Category


class Categories(RequestHandler):
    template = 'category/list.html'

    def get(self):
        self.render(self.template, categories=render_level(self, level=0))


class CategoryLevel(RequestHandler):
    def get(self):
        parent = self.get_argument('parent', None)

        self.write(render_level(self, parent=parent, level=0))


class CategoryHandler(RequestHandler):
    template = 'category/view.html'

    def get(self, id):
        self.render(self.template, category=Category.get(Category.id == id))


def render_level(request, *args, **kwargs):
    template = 'category/blocks/level.html'

    return request.render_string(template, categories=Category.items(*args, **kwargs))