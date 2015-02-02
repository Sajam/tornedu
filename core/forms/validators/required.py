#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..validator import Validator


class RequiredValidator(Validator):
    filters = ['strip', ]

    def validate(self):
        return bool(len(self.value))

    @property
    def error(self):
        return 'Pole {} jest wymagane.'.format(self.field.display_name)