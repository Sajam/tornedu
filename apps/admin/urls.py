from tornado.web import URLSpec
from .handlers import DashboardHandler, ObjectsListHandler


URLS = [
    URLSpec(r'/admin$', DashboardHandler, name='admin_dashboard'),
    URLSpec(r'/admin/objects_list/([a-zA-Z0-9_]+)$', ObjectsListHandler, name='admin_objects_list'),
]