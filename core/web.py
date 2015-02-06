#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado.web import RequestHandler, authenticated
from .db import Db
from .model import Base
from .messages import Messages
from .template_functions import TemplateFunctions


class RequestHandler(RequestHandler):
    template = None

    def prepare(self):
        Db.queries = []
        Base.db = Db.session()

        self.messages = Messages()

    def on_finish(self):
        Base.db.commit()

        print 'Number of executed queries: {}'.format(Db.queries_count())
        # print 'Queries: {}'.format(Db.get_queries())

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

    def redirect(self, url_spec_name_or_url, **kwargs):
        try:
            where = self.reverse_url(url_spec_name_or_url)
        except KeyError:
            where = url_spec_name_or_url

        super(RequestHandler, self).redirect(self.get_argument('next', where), **kwargs)

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