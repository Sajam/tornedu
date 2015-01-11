class FormFieldBase(object):
    type = ''
    form = None

    def __init__(self, field_name, field_value, **field_options):
        self.field_name = field_name
        self.field_value = field_value or ''
        self.field_options = field_options

    def render(self):
        raise NotImplementedError()