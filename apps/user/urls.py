from tornado.web import URLSpec
from .handlers import (
    RegisterHandler, LoginHandler, ProfileHandler, ChangePasswordHandler, ChangeEmailHandler, LogoutHandler
)


URLS = [
    URLSpec(r'/user/user_register$', RegisterHandler, name='user_register'),
    URLSpec(r'/user/login$', LoginHandler, name='user_login'),
    URLSpec(r'/user/profile$', ProfileHandler, name='user_profile'),
    URLSpec(r'/user/change_password$', ChangePasswordHandler, name='user_change_password'),
    URLSpec(r'/user/change_email$', ChangeEmailHandler, name='user_change_email'),
    URLSpec(r'/user/logout$', LogoutHandler, name='user_logout'),
]