from .base import FormFieldBase


class FormFieldText(FormFieldBase):
    def render(self):
        return '<input type="text" name="{}" value="{}">'.format(self.name, self.value)