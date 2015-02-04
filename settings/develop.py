from .base import *

APP['debug'] = True
APP['autoreload'] = True
APP['compiled_template_cache'] = False
APP['static_hash_cache'] = False
APP['serve_traceback'] = True

THREADS = 1

DATABASES['default'] = {
    'connection_string': 'mysql://{user}:{password}@{host}/{dbname}'.format(
        user='tornedu', password='LCA8PKx5nuUjWJUJ', host='localhost', dbname='tornedu'),
    'kwargs': {
        'encoding': 'utf-8',
        # 'echo': True
    }
}