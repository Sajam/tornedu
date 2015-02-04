import functools
import tornado.web
from .db import Db
from .model import Base
from .messages import Messages
from .template_functions import TemplateFunctions


class RequestHandler(tornado.web.RequestHandler):
    template = None

    """
    Extended default Tornado request handler to support new features:
        - self.template_vars storing additional view variables (instead of passing them to render() function),
        - messages system (self.message.[info|warning|error](text)) - automatically renders messages to view,
        - posted() template function that returns posted value - usage in template: {{ posted('email') }},
        - connecting to database and starting session on request, closing session after request is done.
    """
    def __init__(self, *args, **kwargs):
        super(RequestHandler, self).__init__(*args, **kwargs)

        self.db = None
        self.messages = Messages()
        self.current_user_cache = None

    def prepare(self):
        Db.queries = []

        self.db = Db.instance().session()
        Base.db = self.db

    def on_finish(self):
        self.db.commit()
        print 'Queries: {} / {}'.format(Db.instance().queries_count(), Db.instance().get_queries())

    def get(self, *args, **kwargs):
        if self.template:
            self.render(self.template)

    def get_template_namespace(self):
        namespace = super(RequestHandler, self).get_template_namespace()
        namespace.update(TemplateFunctions(self).as_dict())
        namespace['messages'] = self.messages.get_all()

        return namespace

    def posted_model_fields(self, model):
        fields = [column.name for column in model.metadata.tables[model.__tablename__].columns
                  if column.name not in ('id', 'created_at', )]

        return {field: self.get_argument(field, None) for field in fields}

    def redirect(self, url_spec_name_or_url, **kwargs):
        try:
            where = self.reverse_url(url_spec_name_or_url)
        except KeyError:
            where = url_spec_name_or_url

        super(RequestHandler, self).redirect(self.get_argument('next', where), **kwargs)


class AdminRequestHandler(RequestHandler):
    def prepare(self):
        super(AdminRequestHandler, self).prepare()

        if not self.get_current_user() or (self.get_current_user() and not self.get_current_user().is_admin):
            self.redirect('index')


def is_admin(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.current_user or (self.current_user and not self.current_user.is_admin):
            self.redirect('index')

        return method(self, *args, **kwargs)

    return wrapper