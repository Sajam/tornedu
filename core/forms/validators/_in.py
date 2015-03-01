#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..validator import Validator


class InValidator(Validator):
    def validate(self):
        return self.value in self.args[0] if self.args and isinstance(self.args[0], (list, tuple)) else []

    @property
    def error(self):
        return 'Wartość w polu {} nie jest zezwolona.'.format(self.field.display_name)


# File named with _ prefix due to fact that "in" is restricted Python word.
# Eg. "from .in import InValidator" is not valid!