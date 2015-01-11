from .base import ValidatorBase


class ValidatorLength(ValidatorBase):
    filters = ['strip', ]

    def validate(self):
        value_len = len(self.value)

        if 'min' in self.kwargs and value_len < self.kwargs['min']:
            return False
        if 'max' in self.kwargs and value_len > self.kwargs['max']:
            return False

        return True

    @property
    def error(self):
        if 'min' in self.kwargs and 'max' in self.kwargs:
            return 'Length for field {} should be in range {}-{}.'.format(
                self.field_name, self.kwargs['min'], self.kwargs['max'])
        elif 'min' in self.kwargs:
            return 'Min. length for field {} is {}.'.format(self.field_name, self.kwargs['min'])
        elif 'max' in self.kwargs:
            return 'Max. length for field {} is {}.'.format(self.field_name, self.kwargs['max'])