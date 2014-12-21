from tornado.web import URLSpec
from .handlers import LoginHandler, LogoutHandler


URLS = [
    URLSpec(r'/user/login$', LoginHandler, name='user_login'),
    URLSpec(r'/user/logout$', LogoutHandler, name='user_logout'),
]