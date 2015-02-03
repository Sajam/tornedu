#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from tornado.web import authenticated
from core.web import RequestHandler
from .models import User
from .auth import Auth
from .forms import LoginForm, RegisterForm, ChangePasswordForm, ChangeEmailForm


class RegisterHandler(RequestHandler):
    template = 'user/register.html'

    def get(self, *args, **kwargs):
        self.render(self.template, register_form=RegisterForm())

    def post(self, *args, **kwargs):
        form = RegisterForm(self.request.body_arguments)

        if form.validate():
            User(**self.posted_model_fields(User)).save()
            self.messages.success('Rejestracja zakończona sukcesem. Możesz się teraz zalogować.')
        else:
            self.messages.error(form.errors)

        self.render(self.template, register_form=form)


class LoginHandler(RequestHandler, Auth):
    template = 'user/login.html'

    def get(self, *args, **kwargs):
        self.render(self.template, login_form=LoginForm())

    def post(self, *args, **kwargs):
        form = LoginForm(self.request.body_arguments)

        if form.validate():
            try:
                user = User.get(User.name == self.get_argument('name'),
                                User.password == User.hash_password(self.get_argument('password')))

                self.authorize(user)
                self.redirect('index')
            except (MultipleResultsFound, NoResultFound):
                self.messages.error('Użytkownik nie znaleziony lub wprowadzono nieprawidłowe dane.')
        else:
            self.messages.error(form.errors)

        self.render('user/login.html', login_form=form)


class ProfileHandler(RequestHandler):
    template = 'user/profile.html'

    @authenticated
    def get(self, *args, **kwargs):
        self.render(
            self.template,
            change_password_form=ChangePasswordForm(),
            change_email_form=ChangeEmailForm()
        )


class ChangePasswordHandler(ProfileHandler):
    @authenticated
    def post(self, *args, **kwargs):
        form = ChangePasswordForm(self.request.body_arguments, user=self.get_current_user())

        if form.validate():
            user = self.get_current_user()
            user.password = self.get_argument('new')
            user.save()

            self.messages.success('Hasło zostało zmienione.')
        else:
            self.messages.error(form.errors)

        self.render(
            self.template,
            change_password_form=form,
            change_email_form=ChangeEmailForm()
        )


class ChangeEmailHandler(ProfileHandler):
    @authenticated
    def post(self, *args, **kwargs):
        form = ChangeEmailForm(self.request.body_arguments, user=self.get_current_user())

        if form.validate():
            user = self.get_current_user()
            user.email = self.get_argument('email')
            user.save()

            self.messages.success('Adres e-mail został zmieniony.')
        else:
            self.messages.error(form.errors)

        self.render(
            self.template,
            change_password_form=ChangePasswordForm(),
            change_email_form=form
        )


class LogoutHandler(RequestHandler, Auth):
    @authenticated
    def get(self, *args, **kwargs):
        Auth.logout(self)
        self.redirect('index')