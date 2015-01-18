from ..field import FormField


class PasswordField(FormField):
    def render(self):
        return '<input type="password" name="{}">'.format(self.name)