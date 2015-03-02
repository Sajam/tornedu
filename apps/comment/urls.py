#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado.web import URLSpec
from .handlers import CommentHandler


URLS = [
    URLSpec(r'/comment/handler/([0-9]+)$', CommentHandler, name='comment_handler'),
]