from core.forms import *


class RegisterForm(Form):
    fields = [
        FormFieldText('name', validators=[
            ValidatorRequired, ValidatorLength(min=3, max=50)
        ]),
        FormFieldText('email', validators=[
            ValidatorRequired, ValidatorEmail
        ]),
        FormFieldPassword('password', validators=[
            ValidatorRequired
        ]),
        FormFieldPassword('password_confirm', validators=[
            ValidatorEqualFields('password')
        ]),
        FormFieldCheckbox('rules', 'yes', validators=[
            ValidatorChecked, ValidatorEquals('yes')
        ])
    ]