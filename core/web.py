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

    def prepare(self):
        self.db = Db.instance().session()
        Base.db = self.db

    def on_finish(self):
        self.db.commit()

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
                  if column.name not in ('id', )]

        return {field: self.get_argument(field, None) for field in fields}