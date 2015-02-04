#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.web import AdminRequestHandler


class IndexHandler(AdminRequestHandler):
    template = 'admin/index.html'

    def get(self, *args, **kwargs):
        self.render(self.template)