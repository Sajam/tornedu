from tornado.web import URLSpec
from .handlers import IndexHandler


URLS = [
    URLSpec(r'/', IndexHandler, name='index')
]