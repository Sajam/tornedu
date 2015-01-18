from .base import ValidatorBase


class ValidatorEquals(ValidatorBase):
    def validate(self):
        return self.value == self.form.values.get(self.field.name)

    @property
    def error(self):
        return 'Field {} has incorrect value.'.format(self.field.name)