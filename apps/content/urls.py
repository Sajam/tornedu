from tornado.web import URLSpec
from .handlers import CreateContent, ContentTypeForm


URLS = [
    URLSpec(r'/content/create$', CreateContent, name='content_create'),
    URLSpec(r'/content/type/form$', ContentTypeForm, name='content_type_form'),
]