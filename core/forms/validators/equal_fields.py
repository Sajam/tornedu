from .base import ValidatorBase


class ValidatorEqualFields(ValidatorBase):
    def validate(self):
        return self.value == self.field.form.values.get(self.args[0])

    @property
    def error(self):
        return 'Value of {} field is different than {} field value.'.format(
            self.field.name, self.args[0])