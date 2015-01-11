class TemplateFunctions(object):
    def __init__(self, request):
        self.request = request

    def posted(self, key, default=''):
        return self.request.get_argument(key, default)

    def is_active_url(self, url_name, active_class):
        """
        Template helper function for tracking/checking current URL. Example usage:
        <a href="{{ reverse_url('page_contact') }}" class="{{ is_active_url('page_contact', 'active') }}">
        """
        for name, spec in self.request.application.named_handlers.items():
            if name == url_name and isinstance(self, spec.handler_class):
                return active_class

    def as_dict(self):
        return {fnc: getattr(self, fnc) for fnc in dir(self)
                if not fnc.startswith('_') and fnc not in ('request', 'as_dict')}