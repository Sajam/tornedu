import tornado.web
from core.db import Db
from core.model import Base


class RequestHandler(tornado.web.RequestHandler):
    def prepare(self):
        self.db = Db.instance().session()
        Base.db = self.db

    def on_finish(self):
        self.db.commit()

    def get_template_namespace(self):
        namespace = super(RequestHandler, self).get_template_namespace()
        return namespace