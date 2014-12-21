from .base import *

APP['debug'] = True
APP['autoreload'] = True
APP['compiled_template_cache'] = False
APP['static_hash_cache'] = False
APP['serve_traceback'] = True

THREADS = 1