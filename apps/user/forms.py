#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.forms import *
from .models import User


class RegisterForm(Form):
    fields = [
        TextField('name', validators=[
            RequiredValidator, LengthValidator(min=3, max=50)
        ]),
        TextField('email', validators=[
            RequiredValidator, EmailValidator
        ]),
        PasswordField('password', validators=[
            RequiredValidator
        ]),
        PasswordField('password_confirm', validators=[
            EqualFieldsValidator('password')
        ]),
        CheckboxField('rules', 'yes', validators=[
            CheckedValidator, EqualsValidator('yes')
        ])
    ]

    labels = {
        'name': 'Nazwa użytkownika',
        'email': 'E-Mail',
        'password': 'Hasło',
        'password_confirm': 'Potwierdź hasło',
        'rules': 'Akceptuję regulamin'
    }

    @register_validator('name')
    def name_available_validator(self):
        if User.exists(User.name == self.values.get('name')):
            self.add_error('Wybrana nazwa użytkownika jest zajęta.')

    @register_validator('email')
    def email_available_validator(self):
        if User.exists(User.email == self.values.get('email')):
            self.add_error('Podany adres e-mail znajduje się już w naszej bazie danych.')


class LoginForm(Form):
    fields = [
        TextField('name', validators=[RequiredValidator]),
        PasswordField('password', validators=[RequiredValidator])
    ]

    labels = {
        'name': 'Nazwa użytkownika',
        'password': 'Hasło'
    }


class ChangePasswordForm(Form):
    fields = [
        PasswordField('current', validators=[RequiredValidator]),
        PasswordField('new', validators=[RequiredValidator]),
        PasswordField('new_confirm', validators=[EqualFieldsValidator('new')])
    ]

    labels = {
        'current': 'Aktualne hasło',
        'new': 'Nowe hasło',
        'new_confirm': 'Potwierdź nowe hasło'
    }

    @register_validator('current')
    def check_current_password(self):
        if self.extra['user'].password != User.hash_password(self.values.get('current')):
            self.add_error('Aktualne hasło nie jest prawidłowe.')


class ChangeEmailForm(Form):
    fields = [
        TextField('email', validators=[RequiredValidator, EmailValidator])
    ]

    labels = {
        'email': 'Nowy adres e-mail'
    }

    @register_validator('email')
    def check_email_available(self):
        if User.exists(User.id != self.extra['user'].id, User.email == self.values.get('email')):
            self.add_error('Podany adres e-mail znajduje się już w naszej bazie danych.')