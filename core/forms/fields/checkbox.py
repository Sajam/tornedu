from .base import FormFieldBase


class FormFieldCheckbox(FormFieldBase):
    type = 'checkbox'

    def render(self):
        return '<input type="checkbox" name="{}" value="{}" {}>'.format(
            self.field_name,
            self.field_options['value'],
            'checked' if self.is_checked() else ''
        )

    def is_checked(self):
        return self.form.values and self.form.values.get(self.field_name) == self.field_value