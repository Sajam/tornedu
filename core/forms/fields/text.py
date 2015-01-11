from .base import FormFieldBase


class FormFieldText(FormFieldBase):
    type = 'text'

    def render(self):
        return '<input type="text" name="{}" value="{}">'.format(self.field_name, self.field_value)