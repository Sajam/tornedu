from .base import ValidatorBase


class ValidatorRequired(ValidatorBase):
    filters = ['strip', ]

    def validate(self):
        return bool(len(self.value))

    @property
    def error(self):
        return 'Field {} is required.'.format(self.field.name)