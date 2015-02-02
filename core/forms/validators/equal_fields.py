#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..validator import Validator


class EqualFieldsValidator(Validator):
    def validate(self):
        return self.value == self.field.form.values.get(self.args[0])

    @property
    def error(self):
        return 'Wartość w polu {} różni się od wartości w polu {}.'.format(
            self.field.display_name, self.args[0])