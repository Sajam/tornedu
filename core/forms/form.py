from .fields import *


class Form(object):
    default_field_type = 'text'
    fields = {}

    def __init__(self, values=None):
        self.defined_fields = {
            field_type.type: field_type
            for field_type in FormFieldBase.__subclasses__()
        }

        self.original_values = values
        self.values = {
            key: self.field_value(key)
            for key in values.iterkeys()
        } if isinstance(values, dict) else None
        self.validated = False
        self.errors_list = []

    def validate(self):
        if not self.validated:
            for field_name, field_options in self.fields.iteritems():
                if 'validators' in field_options:
                    for validator in field_options['validators']:
                        validator_instance = None
                        if isinstance(validator, type):
                            validator_instance = validator(
                                field_name,
                                field_options,
                                self.field_value(field_name)
                            )
                        elif self.values:
                            validator_instance = validator
                            validator_instance.lazy_init(
                                field_name,
                                field_options,
                                self.field_value(field_name)
                            )

                        validator_instance.form = self

                        if validator_instance and not validator_instance.validate():
                            self.errors_list.append(validator_instance.error)

            self.validated = True

        return True if not bool(len(self.errors_list)) else False

    def field_value(self, field_name):
        try:
            if not field_name.endswith('[]'):
                return self.original_values[field_name][0]
            else:
                return self.original_values[field_name]
        except (TypeError, KeyError, AttributeError):
            return None

    def html(self):
        result = ''

        for field_name, field_options in self.fields.iteritems():
            if 'type' not in field_options:
                field_options['type'] = self.default_field_type

            field_instance = self.defined_fields[field_options['type']](
                field_name,
                self.field_value(field_name),
                **field_options
            )

            field_instance.form = self

            result += field_instance.render()

        return result

    def errors(self):
        if not self.validated:
            self.validate()

        return self.errors_list if bool(len(self.errors_list)) else False

    def __repr__(self):
        return self.html()