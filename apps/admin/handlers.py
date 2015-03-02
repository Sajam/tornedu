#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.web import AdminRequestHandler
from .utils import AdminUtils


class DashboardHandler(AdminRequestHandler):
    template = 'admin/dashboard.html'

    def get(self):
        models = []

        for model_name, model in AdminUtils.models.iteritems():
            models.append({
                'name': model_name,
                'model': model,
                'url': (self.reverse_url('admin_objects_list', model_name)
                        if model_name not in AdminUtils.models_handlers else
                        self.reverse_url(AdminUtils.models_handlers[model_name]))
            })

        self.render(self.template, models=models)


class ObjectsListHandler(AdminRequestHandler):
    template = 'admin/objects_list.html'

    def get(self, model_name):
        model = AdminUtils.models[model_name]
        fields = [column.name for column in model.__mapper__.columns if column.name not in ('password', )]
        rows = model.query().all()

        self.render(self.template, model=model, fields=fields, rows=rows)