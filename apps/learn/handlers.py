#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.web import RequestHandler
from .forms import LearnForm


class LearnHandler(RequestHandler):
    template = 'learn/view.html'

    def get(self):
        self.render(self.template, learn_form=LearnForm())

    def post(self):
        self.render(self.template, learn_form=LearnForm(self.request.body_arguments))