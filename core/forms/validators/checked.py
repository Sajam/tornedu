from ..validator import Validator


class CheckedValidator(Validator):
    def validate(self):
        return bool(self.form.values.get(self.field.name))

    @property
    def error(self):
        return 'Field {} is not checked.'.format(self.field.name)