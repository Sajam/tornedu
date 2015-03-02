import os

# Tornado application configuration http://tornado.readthedocs.org/en/latest/web.html#application-configuration
# static_path and template_path will be added automatically if STATIC_PATH or TEMPLATE_PATH are defined in settings.
APP = {
    'cookie_secret': 'm/]*EqjW;K-B6fxObtb[]*)gQ%kVhr+Y7h}^J*]}$3Z&@9vuuE8,Fvihkdk>ek?',
    'xsrf_cookies': True,
    'login_url': '/user/login',
}

# http://tornado.readthedocs.org/en/latest/tcpserver.html#tornado.tcpserver.TCPServer.listen
PORT = 8888

# Number of server child processes to run.
# Value <= 0 forks one process per CPU.
# http://tornado.readthedocs.org/en/latest/tcpserver.html#tornado.tcpserver.TCPServer.start
NUM_PROCESSES = 0

# Paths specifying where to search for classes.
LOADER_PATHS = {
    'models': [
        'apps.*.models',
    ],
    'management': [
        'core.management.commands.*',
        'apps.management.*',
    ],
}

# URLs gonna be populated automatically by collecting URL-s defined in enabled apps.
URLS = []

# List of databases.
DATABASES = {
    'default': {
        'driver': 'sqlite',
        'database': ':memory:'
    }
}

# Name of database that should be used by default.
DATABASE = 'default'

# List of enabled apps.
APPS = [
    'admin',
    'index',
    'user',
    'category',
    'content',
    'comment',
]

# Main project directory.
BASE_PATH = os.path.join(os.path.dirname(__file__), '..')

# Tornado static path.
STATIC_PATH = os.path.join(BASE_PATH, 'static')

# Tornado templates path.
TEMPLATE_PATH = os.path.join(BASE_PATH, 'templates')

MESSAGE_TYPES = ('success', 'info', 'warning', 'error', )