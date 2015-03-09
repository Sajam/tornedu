#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado.web import URLSpec
from .handlers import LearnHandler


URLS = [
    URLSpec(r'/learn/handler/([0-9]+)$', LearnHandler, name='learn_handler'),
]