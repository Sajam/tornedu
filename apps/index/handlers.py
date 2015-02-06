#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.web import RequestHandler


class IndexHandler(RequestHandler):
    template = 'index/index.html'