#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from ..validator import Validator


class RegexValidator(Validator):
    def validate(self):
        return re.match(self.regex, self.value)

    @property
    def error(self):
        return 'Wartość w polu {} ma niepoprawny format.'.format(self.field.display_name)