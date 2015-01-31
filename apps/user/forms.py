#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.forms import *
from apps.user.models import User


class LoginForm(Form):
    fields = [
        TextField('name', validators=[RequiredValidator]),
        PasswordField('password', validators=[RequiredValidator])
    ]

    labels = {
        'name': 'Nazwa użytkownika',
        'password': 'Hasło'
    }


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

    @register_validator('name')
    def name_available_validator(self):
        if User.exists(User.name == self.values.get('name')):
            self.add_error('Wybrana nazwa użytkownika jest zajęta.')

    @register_validator('email')
    def email_available_validator(self):
        if User.exists(User.email == self.values.get('email')):
            self.add_error('Podany adres e-mail znajduje się już w naszej bazie danych.')

    labels = {
        'name': 'Nazwa użytkownika',
        'email': 'E-Mail',
        'password': 'Hasło',
        'password_confirm': 'Potwierdź hasło',
        'rules': 'Akceptuję regulamin'
    }