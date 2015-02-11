from tornado.web import URLSpec
from .admin import CategoriesAdminHandler


URLS = [
    URLSpec(r'/admin/categories$', CategoriesAdminHandler, name='admin_categories'),
]