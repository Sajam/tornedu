#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.web import RequestHandler
from .forms import CommentForm


class CommentHandler(RequestHandler):
    template = 'comment/view.html'

    def get(self):
        self.render(self.template, comment_form=CommentForm())

    def post(self):
        self.render(self.template, comment_form=CommentForm(self.request.body_arguments))


def comments_view(request, content):
    template = 'comment/view.html'

    return request.render_string(
        template,
        content=content,
        comments=content.comments,
        form=CommentForm()
    )