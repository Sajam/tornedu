#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..field import FormField


class PasswordField(FormField):
    def render(self):
        return '<input type="password" name="{}">'.format(self.name)