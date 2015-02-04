from tornado.web import URLSpec
from .handlers import IndexHandler


URLS = [
    URLSpec(r'/admin$', IndexHandler, name='admin_index'),
]