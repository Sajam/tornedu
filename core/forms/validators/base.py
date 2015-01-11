from .filters import ValidatorFilters


class ValidatorBase(object):
    form = None
    filters = []
    defined_filters = ValidatorFilters.filters()

    def __init__(self, field_name=None, field_options=None, value=None, **kwargs):
        self.kwargs = kwargs

        if field_name and field_options:
            self.lazy_init(field_name, field_options, value)

    def lazy_init(self, field_name, field_options, value):
        self.field_name = field_name
        self.field_options = field_options
        self.original_value = value
        self.value = value

        for validator_filter in self.filters:
            if validator_filter in self.defined_filters.keys():
                self.value = self.defined_filters[validator_filter](self.value)

    def prepare(self):
        pass

    def validate(self):
        raise NotImplementedError()

    @property
    def default_error(self):
        return 'Value {} for field is not valid.'.format(self.original_value, self.field_name)