#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..validator import Validator


class LengthValidator(Validator):
    filters = ['strip', ]

    def validate(self):
        length = len(self.value)

        return not ((getattr(self, 'min') and length < self.min) or (
            getattr(self, 'max') and length > self.max))

    @property
    def error(self):
        if getattr(self, 'min') and getattr(self, 'max'):
            return 'Długość wartość w polu {} powinna się mieścić w {}-{} znakach.'.format(
                self.field.display_name, self.min, self.max)

        elif getattr(self, 'min'):
            return 'Min. wymagana długość dla pola {} to {} znaków.'.format(self.field.display_name, self.min)

        elif getattr(self, 'max'):
            return 'Max. dozwolona długość dla pola {} to {} znaków.'.format(self.field.display_name, self.max)