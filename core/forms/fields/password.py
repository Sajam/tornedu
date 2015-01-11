from .base import FormFieldBase


class FormFieldPassword(FormFieldBase):
    type = 'password'

    def render(self):
        return '<input type="password" name="{}">'.format(self.field_name)