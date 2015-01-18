from core.forms import *


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