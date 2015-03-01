from tornado.web import URLSpec
from .admin import CategoriesAdminHandler, CategoryAddHandler, CategoryDeleteHandler, CategoryEditHandler
from .handlers import Categories, CategoryLevel, CategoryHandler


URLS = [
    URLSpec(r'/categories$', Categories, name='categories'),
    URLSpec(r'/category/level$', CategoryLevel, name='category_level'),
    URLSpec(r'/category/([0-9]+)$', CategoryHandler, name='category'),
    URLSpec(r'/admin/categories$', CategoriesAdminHandler, name='admin_categories'),
    URLSpec(r'/admin/category/add$', CategoryAddHandler, name='admin_category_add'),
    URLSpec(r'/admin/category/delete$', CategoryDeleteHandler, name='admin_category_delete'),
    URLSpec(r'/admin/category/edit$', CategoryEditHandler, name='admin_category_edit'),
]