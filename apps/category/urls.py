from tornado.web import URLSpec
from .admin import CategoriesAdminHandler, CategoryAddHandler


URLS = [
    URLSpec(r'/admin/categories$', CategoriesAdminHandler, name='admin_categories'),
    URLSpec(r'/admin/category/add$', CategoryAddHandler, name='admin_category_add'),
]