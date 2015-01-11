from core.forms import *


class RegisterForm(Form):
    fields = {
        'name': {
            'type': 'text',
            'validators': [
                ValidatorRequired, ValidatorLength(min=3, max=50)
            ]
        },
        'password': {
            'type': 'password',
            'validators': [
                ValidatorRequired
            ]
        },
        'password_confirm': {
            'type': 'password',
            'validators': [
                ValidatorSameAs(field='password')
            ]
        },
        'rules': {
            'type': 'checkbox',
            'value': 'yes',
            'validators': [
                ValidatorChecked
            ]
        }
    }