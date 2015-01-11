from .base import ValidatorBase


class ValidatorChecked(ValidatorBase):
    def validate(self):
        return self.field_options['value'] == self.form.values.get(self.field_name)

    @property
    def error(self):
        return 'Field {} is not checked.'.format(self.field_name)