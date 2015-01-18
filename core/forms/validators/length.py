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
            return 'Value length for field {} can be in range {}-{}.'.format(
                self.field.name, self.min, self.max)

        elif getattr(self, 'min'):
            return 'Min. length required for field {} is {}.'.format(self.field.name, self.min)

        elif getattr(self, 'max'):
            return 'Max. allowed length for field {} is {}.'.format(self.field.name, self.max)