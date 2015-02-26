from .base import *

# If in Tornado application is in debug mode autoreload is enabled.
# If autoreload is enabled number of threads must be 1.
# http://tornado.readthedocs.org/en/latest/guide/running.html#debug-mode
NUM_PROCESSES = 1

# http://tornado.readthedocs.org/en/latest/guide/running.html#debug-mode
APP['debug'] = True

DATABASES['default'] = {
    'driver': 'mysql',
    'username': 'tornedu',
    'password': 'LCA8PKx5nuUjWJUJ',
    'host': 'localhost',
    'database': 'tornedu',
    'options': {
        # http://docs.sqlalchemy.org/en/rel_0_9/dialects/mysql.html#connection-timeouts
        'pool_recycle': 3600,
    }
}