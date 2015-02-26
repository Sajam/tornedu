#!/usr/bin/env python
# -*- coding: utf-8 -*-
import types
from tornado.web import RequestHandler, authenticated
from .database import Database
from .model import BaseModel
from .messages import Messages
from .template_functions import TemplateFunctions
from .utils import log
from apps.user.auth import Auth


class RequestHandler(RequestHandler, Auth):
    template = None

    def prepare(self):
        BaseModel.db_session = Database.instance().make_session()
        self.messages = Messages()

    def on_finish(self):
        BaseModel.db_session.commit()
        queries_count = Database.queries_count()
        log('{} {} executed'.format(queries_count, ['queries', 'query'][queries_count == 1]))
        log('Queries', show_datetime=False, data=Database.get_queries())

    @property
    def current_user(self):
        if not hasattr(self, '_current_user'):
            self._current_user = self.get_current_user()

        return self._current_user

    def get_template_namespace(self):
        namespace = super(RequestHandler, self).get_template_namespace()

        namespace.update(TemplateFunctions(self).as_dict())
        namespace['messages'] = self.messages.get_all()

        return namespace

    def get(self):
        if self.template:
            self.render(self.template)

    def redirect(self, target, **kwargs):
        remembered_redirect = self.get_argument('next', False)

        if remembered_redirect:
            where = remembered_redirect
        else:
            try:
                where = self.reverse_url(target)
            except KeyError:
                where = target

        super(RequestHandler, self).redirect(where, **kwargs)

    # Allow to pass handler class as argument (name).
    def reverse_url(self, name, *args):
        if isinstance(name, (type, types.ClassType)) and issubclass(name, (RequestHandler, AdminRequestHandler)):
            for url_name, spec in self.application.named_handlers.iteritems():
                if spec.handler_class == name:
                    name = url_name
                    break

        return super(RequestHandler, self).reverse_url(name, *args)

    # Return all POST fields for specified model (but only relevant eg. no id or created_at).
    def posted_model_fields(self, model):
        return {
            field: self.get_argument(field, None) for field in [
                field.name for field in model.fields() if field.name not in ('id', 'created_at', )
            ]
        }

    # Just to avoid IDE "must implement all abstract methods" warning.
    def data_received(self, chunk):
        pass


class AdminRequestHandler(RequestHandler):
    def prepare(self):
        super(AdminRequestHandler, self).prepare()

        if not self.current_user or (self.current_user and not self.current_user.is_admin):
            self.redirect('index')