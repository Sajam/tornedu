#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..validator import Validator


class EqualsValidator(Validator):
    def validate(self):
        return self.value == self.form.values.get(self.field.name)

    @property
    def error(self):
        return 'Pole {} ma niepoprawną wartość.'.format(self.field.display_name)