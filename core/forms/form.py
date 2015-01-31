from collections import defaultdict
import os
from compiler.ast import flatten
from tornado.template import Loader
from core.conf import Settings


class Form(object):
    # Form's fields defined in subclasses.
    fields = []
    labels = {}
    templates_path = os.path.join(Settings.TEMPLATE_PATH, 'form')
    template = 'form.html'
    display_all_errors_for_field = False

    def __init__(self, values=None):
        self.values = Form.parse_values(values or {})
        self.errors_list = []
        self.fields = [field.prepare(self) for field in self.fields]
        self.extra_validators = self.get_extra_validators()

    def get_extra_validators(self):
        extra_validators = defaultdict(list)

        for method_name in dir(self):
            method = getattr(self, method_name)
            if hasattr(method, 'is_extra_validator'):
                extra_validators[getattr(method, 'is_extra_validator')].append(method)

        return extra_validators

    def validate(self):
        for field in self.fields:
            if not field.validate():
                self.errors_list += flatten([field.errors])

        for field_name, extra_validators in self.extra_validators.iteritems():
            for extra_validator in extra_validators:
                extra_validator()

        return not bool(len(self.errors_list))

    def add_error(self, error_message):
        self.errors_list += [error_message]

    @property
    def errors(self):
        return self.errors_list if len(self.errors_list) else False

    def render(self):
        return Loader(self.templates_path).load(self.template).generate(
            form=self,
            fields=self.fields,
            labels=self.labels
        )

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


def register_validator(name):
    def wrapper(validator_function):
        validator_function.is_extra_validator = name
        return validator_function

    return wrapper