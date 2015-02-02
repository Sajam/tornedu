from tornado.web import URLSpec
from .handlers import LoginHandler, LogoutHandler, RegisterHandler, ProfileHandler


URLS = [
    URLSpec(r'/user/login$', LoginHandler, name='user_login'),
    URLSpec(r'/user/profile$', ProfileHandler, name='user_profile'),
    URLSpec(r'/user/logout$', LogoutHandler, name='user_logout'),
    URLSpec(r'/user/user_register$', RegisterHandler, name='user_register'),
]