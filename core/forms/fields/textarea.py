from ..field import FormField


class TextareaField(FormField):
    def render(self):
        return '<textarea name="{}">{}</textarea>'.format(self.name, self.value)