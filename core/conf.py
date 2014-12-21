import os

environment = os.environ.get('TORNADO_ENVIRONMENT', 'stable')
Settings = __import__('settings.{}'.format(environment), globals(), locals(), [environment])

for app in Settings.APPS:
    try:
        app = __import__('apps.{}.urls'.format(app), globals(), locals(), ['URLS'])
        Settings.URLS += app.URLS
    except ImportError:
        pass