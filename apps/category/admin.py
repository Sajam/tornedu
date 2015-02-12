#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from core.web import AdminRequestHandler
from .models import Category


class CategoriesAdminHandler(AdminRequestHandler):
    model = Category
    template = 'category/admin.html'

    def get(self):
        rows = Category.query().all()
        self.render(self.template, categories=rows)


class CategoryAddHandler(AdminRequestHandler):
    def post(self):
        parent = self.get_argument('parent', None)
        category = Category(name=self.get_argument('name', ''), parent=int(parent) if parent else None).save()

        self.write(json.dumps({'id': category.id}))