from compiler.ast import flatten


class Form(object):
    # Form's fields defined in subclasses.
    fields = {}
    display_all_errors_for_field = False

    def __init__(self, values=None):
        self.values = Form.parse_values(values or {})
        self.errors_list = []
        self.fields = [field.prepare(self) for field in self.fields]

    def validate(self):
        for field in self.fields:
            if not field.validate():
                self.errors_list += flatten([field.errors])

        return not bool(len(self.errors_list))

    @property
    def errors(self):
        return self.errors_list if len(self.errors_list) else False

    def render(self):
        result = ''

        for field in self.fields:
            result += field.render()

        return result

    def __repr__(self):
        return self.render()

    @staticmethod
    def parse_values(values):
        parsed_values = {}

        for name, value in values.iteritems():
            if name.endswith('[]'):
                parsed_values[name[:-2]] = value
            else:
                parsed_values[name] = value[0]

        return parsed_values