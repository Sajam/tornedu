import os

BASE_PATH = os.path.join(os.path.dirname(__file__), '..')
STATIC_PATH = os.path.join(BASE_PATH, 'static')
TEMPLATE_PATH = os.path.join(BASE_PATH, 'templates')


PORT = 8888

APP = {
    'static_path': STATIC_PATH,
    'template_path': TEMPLATE_PATH,
    'cookie_secret': 'm/]*EqjW;K-B6fxObtb[]*)gQ%kVhr+Y7h}^J*]}$3Z&@9vuuE8,Fvihkdk>ek?',
    'xsrf_cookies': True
}

THREADS = 0  # Forks one process per CPU.

APPS = [
    'index',
    'user',
]

URLS = []

DATABASES = {
    'default': {
        'connection_string': 'sqlite:///:memory:'
    }
}