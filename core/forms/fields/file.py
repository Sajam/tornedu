#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..field import FormField


class FileField(FormField):
    def render(self):
        return '<input type="file" name="{}">'.format(self.name)