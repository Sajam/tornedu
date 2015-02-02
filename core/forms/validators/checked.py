#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..validator import Validator


class CheckedValidator(Validator):
    def validate(self):
        return bool(self.form.values.get(self.field.name))

    @property
    def error(self):
        return 'Pole {} nie jest zaznaczone.'.format(self.field.display_name)