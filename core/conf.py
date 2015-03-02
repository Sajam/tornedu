#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from core.utils import import_class_from_path


environment = os.environ.get('TORNADO_ENVIRONMENT_FORCE', os.environ.get('TORNADO_ENVIRONMENT', 'stable'))
Settings = import_class_from_path(environment, 'settings')


# Validating settings.
if hasattr(Settings, 'DATABASES') and hasattr(Settings, 'DATABASE') and Settings.DATABASE not in Settings.DATABASES:
    available_databases = Settings.DATABASES.keys()

    raise Exception(
        'Database configuration "{}" specified as default database in settings (DATABASE) not exists.'
        'Available databases: {}'.format(
            Settings.DATABASE,
            ', '.join(available_databases) if available_databases else '(none)'
        )
    )

if 'debug' in Settings.APP and Settings.APP['debug'] and Settings.NUM_PROCESSES != 1:
    raise Exception('NUM_PROCESSES option in settings must be 1 if Tornado application debug mode is enabled.')


# Additional auto-generated settings variables.
Settings.ENVIRONMENT = environment
Settings.USING_DATABASE = hasattr(Settings, 'DATABASES') and hasattr(Settings, 'DATABASE') and Settings.DATABASE in Settings.DATABASES
Settings.DEFAULT_DATABASE_SETTINGS = Settings.DATABASES[Settings.DATABASE] if Settings.USING_DATABASE else None

if hasattr(Settings, 'STATIC_PATH'):
    Settings.APP['static_path'] = Settings.STATIC_PATH

if hasattr(Settings, 'TEMPLATE_PATH'):
    Settings.APP['template_path'] = Settings.TEMPLATE_PATH


# Collecting all URLS to pass them later to application when it starts.
for app_name in Settings.APPS:
    app_urls = import_class_from_path('urls', 'apps.{}'.format(app_name))
    if app_urls:
        Settings.URLS += app_urls.URLS