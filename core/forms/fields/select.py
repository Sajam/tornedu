import types
from collections import OrderedDict
from ..field import FormField


class SelectField(FormField):
    def __init__(self, name, options=None, *args, **kwargs):
        self._options = options
        self._blank = kwargs.get('blank')

        super(SelectField, self).__init__(name, *args, **kwargs)

    def render(self):
        return '<select name="{}">{}</select>'.format(
            self.name,
            ''.join(['<option value="{}" {}>{}</option>'.format(k, 'selected' if str(k) == str(self.value) else '', v)
                     for k, v in self.options.iteritems()])
        )

    @property
    def options(self):
        options = OrderedDict()

        if self._blank:
            options.update({'': self._blank})

        if self._options:
            if isinstance(self._options, types.FunctionType):
                options.update(self._options())
            else:
                options.update(self._options)

        return options