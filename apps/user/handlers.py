#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from tornado.web import authenticated
from core.web import RequestHandler
from .models import User
from .auth import Auth
from .forms import LoginForm, RegisterForm


class LoginHandler(RequestHandler, Auth):
    template = 'user/login.html'

    def get(self, *args, **kwargs):
        self.render(self.template, login_form=LoginForm())

    def post(self, *args, **kwargs):
        form = LoginForm(self.request.body_arguments)

        if form.validate():
            try:
                user = User.get(User.name == self.get_argument('name'),
                                User.password == hashlib.md5(self.get_argument('password')).hexdigest())

                self.authorize(user)
                self.redirect(self.get_argument('next', self.reverse_url('index')))
            except (MultipleResultsFound, NoResultFound):
                self.messages.error('Użytkownik nie znaleziony lub wprowadzono nieprawidłowe dane.')
        else:
            self.messages.error(form.errors)

        self.render('user/login.html', login_form=form)


class LogoutHandler(RequestHandler, Auth):
    @authenticated
    def get(self, *args, **kwargs):
        Auth.logout(self)
        self.redirect(self.get_argument('next', self.reverse_url('index')))


class RegisterHandler(RequestHandler):
    template = 'user/register.html'

    def get(self, *args, **kwargs):
        self.render(self.template, register_form=RegisterForm())

    def post(self, *args, **kwargs):
        form = RegisterForm(self.request.body_arguments)

        if form.validate():
            User(**self.posted_model_fields(User)).save()
            self.messages.success('Rejestracja zakończona sukcesem. Możesz się teraz zalogować.')
            form.clear()
        else:
            self.messages.error(form.errors)

        self.render(self.template, register_form=form)


class ProfileHandler(RequestHandler):
    template = 'user/profile.html'

    @authenticated
    def get(self, *args, **kwargs):
        pass

    @authenticated
    def post(self, *args, **kwargs):
        pass