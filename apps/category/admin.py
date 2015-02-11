#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.web import AdminRequestHandler
from .models import Category


class CategoriesAdminHandler(AdminRequestHandler):
    model = Category
    template = 'category/admin.html'

    def get(self):
        rows = Category.query().all()
        self.render(self.template, categories=rows)