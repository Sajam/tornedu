from .base import FormFieldBase


class FormFieldPassword(FormFieldBase):
    def render(self):
        return '<input type="password" name="{}">'.format(self.name)