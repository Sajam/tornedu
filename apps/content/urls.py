#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado.web import URLSpec
from .handlers import CreateContent, ContentTypeForm, ContentView


URLS = [
    URLSpec(r'/content/create$', CreateContent, name='content_create'),
    URLSpec(r'/content/type/form$', ContentTypeForm, name='content_type_form'),
    URLSpec(r'/content/view/([0-9]+)$', ContentView, name='content_view'),
]