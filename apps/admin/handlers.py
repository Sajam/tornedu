#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.web import AdminRequestHandler
from .utils import AdminUtils


class DashboardHandler(AdminRequestHandler):
    template = 'admin/dashboard.html'

    def get(self):
        self.render(self.template, models=AdminUtils.models)


class ObjectsListHandler(AdminRequestHandler):
    template = 'admin/objects_list.html'

    def get(self, model_name):
        model = AdminUtils.models[model_name]
        fields = model.fields()
        rows = model.query().all()

        self.render(self.template, model=model, fields=fields, rows=rows)