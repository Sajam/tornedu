import os

environment = os.environ.get('TORNADO_ENVIRONMENT', 'stable')
Settings = __import__('settings.{}'.format(environment), fromlist=[environment])

# Collecting all URLS to pass them later to application when it starts.
for app in Settings.APPS:
    try:
        app = __import__('apps.{}.urls'.format(app), fromlist=['URLS'])
        Settings.URLS += app.URLS
    except ImportError:
        pass