from tornado.web import URLSpec
from .handlers import CreateContent


URLS = [
    URLSpec(r'/content/create$', CreateContent, name='content_create'),
]