#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..field import FormField


class CheckboxField(FormField):
    template = 'fields/checkbox.html'

    def __init__(self, name, checkbox_value, *args, **kwargs):
        super(CheckboxField, self).__init__(name, checkbox_value=checkbox_value, *args, **kwargs)

    def render(self):
        return '<input type="checkbox" name="{}" value="{}" {}>'.format(
            self.name,
            self.checkbox_value,
            'checked' if self.is_checked() else ''
        )

    def is_checked(self):
        return self.value == self.checkbox_value