from compiler.ast import flatten
from bs4 import BeautifulSoup
from tornado.template import Loader
from .validators.required import RequiredValidator


class FormField(object):
    id = 0
    template = 'fields/basic.html'

    def __init__(self, name, *args, **kwargs):
        FormField.id += 1

        self.id = 'field-{}'.format(FormField.id)
        self.form = None
        self.name = name
        self.initial_value = None
        self.value = None
        self.validators = []
        self.errors_list = []

        for name, value in kwargs.iteritems():
            setattr(self, name, value)

    def prepare(self, form):
        self.form = form
        self.value = self.form.values.get(self.name, self.initial_value) or ''
        self.validators = [(validator() if type(validator) == type else validator).prepare(self)
                           for validator in self.validators]
        self.errors_list = []

        return self

    def validate(self):
        required_validator = filter(lambda v: isinstance(v, RequiredValidator), self.validators)

        # If there is no RequiredValidator run validators only if there is any value. If RequiredValidator run all.
        if required_validator or (not required_validator and self.value):
            for validator in self.validators:
                if not validator.validate_base():
                    self.errors_list += flatten([validator.errors])

        return not bool(len(self.errors_list))

    def clear(self):
        self.value = self.initial_value or ''

    @property
    def errors(self):
        return (self.errors_list if self.get_option('display_all_errors_for_field') else self.errors_list[0]) \
            if len(self.errors_list) else False

    @property
    def display_name(self):
        return self.form.labels.get(self.name, self.name).lower()

    def render_base(self):
        html = BeautifulSoup(Loader(self.form.templates_path).load(self.template).generate(
            form=self.form,
            field=self
        ))

        for field_html in html.find_all('input'):
            field_html['id'] = self.id

        return html

    # Subclasses should implement this method and return form field's HTML.
    def render(self):
        raise NotImplementedError()

    def get_option(self, name):
        return getattr(self, name, getattr(self.form, name))