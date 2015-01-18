from ..field import FormField


class TextField(FormField):
    def render(self):
        return '<input type="text" name="{}" value="{}">'.format(self.name, self.value)