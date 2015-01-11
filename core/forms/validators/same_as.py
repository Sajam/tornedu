from .base import ValidatorBase


class ValidatorSameAs(ValidatorBase):
    def validate(self):
        return self.value == self.form.values[self.kwargs['field']]

    @property
    def error(self):
        return 'Field {} is not the same as {}.'.format(self.field_name, self.kwargs['field'])