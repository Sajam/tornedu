#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.web import RequestHandler, authenticated


class CreateContent(RequestHandler):
    template = 'content/create.html'

    @authenticated
    def get(self):
        self.render(self.template)