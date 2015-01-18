from ..validator import Validator


class RequiredValidator(Validator):
    filters = ['strip', ]

    def validate(self):
        return bool(len(self.value))

    @property
    def error(self):
        return 'Field {} is required.'.format(self.field.name)