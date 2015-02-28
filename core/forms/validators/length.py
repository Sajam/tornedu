#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..validator import Validator


class LengthValidator(Validator):
    filters = ['strip', ]

    def validate(self):
        length = len(self.value)

        return not ((hasattr(self, 'min') and length < self.min) or (
            hasattr(self, 'max') and length > self.max))

    @property
    def error(self):
        if hasattr(self, 'min') and hasattr(self, 'max'):
            return 'Długość wartość w polu {} powinna się mieścić w {}-{} znakach.'.format(
                self.field.display_name, self.min, self.max)

        elif hasattr(self, 'min'):
            return 'Min. wymagana długość dla pola {} to {} znaków.'.format(self.field.display_name, self.min)

        elif hasattr(self, 'max'):
            return 'Max. dozwolona długość dla pola {} to {} znaków.'.format(self.field.display_name, self.max)