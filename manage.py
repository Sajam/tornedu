#!/usr/bin/env python
import os
import sys

# Text displayed when there is no action specified or specified action is not supported.
help_text = 'Available commands:\n' \
            '\tcreate_schema - drop existing tables and create schema basing on models\n\n' \
            'Options:\n' \
            '\t--settings=name - force management script to use specified settings'

# Check whether action is specified, if no display help text.
if len(sys.argv) < 2:
    exit(help_text)

# Find, parse and handle arguments.
args = []
for arg in sys.argv:
    if arg.startswith('--'):
        name, value = arg[2:].split('=', 1) if '=' in arg else [arg[2:], None]

        # Force management script to use specified settings.
        if name == 'settings' and value:
            os.environ['TORNADO_ENVIRONMENT_FORCE'] = value
    else:
        args.append(arg)


from core.conf import Settings
print 'Using "{}" settings (environment).'.format(Settings.ENVIRONMENT)

try:
    if args[1] == 'create_schema':
        from core.utils import import_class_from_path
        from core.database import Database
        from core.model import *

        Database.instance().connect(Settings.DEFAULT_DATABASE_SETTINGS)
        db_engine = Database.instance().engine

        for app in Settings.APPS:
            import_class_from_path('models', 'apps.{}'.format(app))

        BaseModel.metadata.drop_all(db_engine, checkfirst=False)
        BaseModel.metadata.create_all(db_engine, checkfirst=False)

        print 'Created database schema.'
finally:
    # Restore default settings by removing forced settings variable.
    if 'TORNADO_ENVIRONMENT_FORCE' in os.environ:
        del os.environ['TORNADO_ENVIRONMENT_FORCE']

    exit()