from ..validator import Validator


class EqualsValidator(Validator):
    def validate(self):
        return self.value == self.form.values.get(self.field.name)

    @property
    def error(self):
        return 'Field {} has incorrect value.'.format(self.field.name)