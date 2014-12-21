from tornado.web import URLSpec
from .handlers import LoginHandler


URLS = [
    URLSpec(r'/user/login$', LoginHandler, name='user_login')
]