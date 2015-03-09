#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.web import RequestHandler, authenticated, ajax
from .forms import ContentForm, content_types_forms
from .models import Content, content_types
from apps.comment.handlers import comments_view


class CreateContent(RequestHandler):
    template = 'content/create.html'

    @authenticated
    def get(self):
        self.render(self.template, content_form=ContentForm(), content_type_form='')

    @authenticated
    def post(self):
        content_type = self.get_argument('type', None)
        content_form = ContentForm(self.submitted_data)
        content_type_form = None
        errors = []

        if not content_form.validate():
            errors += content_form.errors

        if content_type and content_type in content_types:
            content_type_form = content_types_forms[content_type](self.request.body_arguments)
            if not content_type_form.validate():
                errors += content_type_form.errors

        if errors:
            self.messages.error(errors)
        else:
            content_form.clear()
            content_type_form.clear()

            content_type_model = content_types[content_type]
            content_type_entry = content_type_model(**self.posted_model_fields(content_type_model))
            content_type_entry.user = self.current_user.id

            if self.current_user.is_admin:
                content_type_entry.visible = True

            content_type_entry.save()

            self.messages.success('Treść dodana poprawnie!')

        self.render(self.template, content_form=content_form, content_type_form=content_type_form or '')


class ContentTypeForm(RequestHandler):
    @ajax
    @authenticated
    def get(self):
        content_type = self.get_argument('type', None)

        if content_type and content_type in content_types and content_type in content_types_forms:
            return self.write(content_types_forms[content_type]().render())
        else:
            raise Exception('Nieznany typ treści.')


class ContentView(RequestHandler):
    template = 'content/view.html'

    def get(self, id):
        content = Content.get(Content.id == id)
        if (self.current_user and self.current_user.is_admin) or content.visible:
            content.views += 1
            content.save()

            self.render(
                self.template,
                content=content,
                comments=comments_view(self, content)
            )
        else:
            self.messages.info('Wybrana treść jest ukryta.')