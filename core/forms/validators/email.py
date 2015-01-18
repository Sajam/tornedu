from lepl.apps.rfc3696 import Email
from ..validator import Validator


class EmailValidator(Validator):
    filters = ['strip', ]

    def validate(self):
        email_validator = Email()
        return email_validator(self.value)

    @property
    def error(self):
        return '{} is not valid e-mail.'.format(self.value if len(self.value) else '(blank)')