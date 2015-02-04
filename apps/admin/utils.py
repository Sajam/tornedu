from core.conf import Settings


class AdminUtils(object):
    apps = {}

    def __init__(self):
        self.prepare_apps()

    def prepare_apps(self):
        used_models = []

        for app in Settings.APPS:
            AdminUtils.apps[app] = {}

            try:
                models = __import__('apps.{}.models'.format(app), fromlist=['apps.{}'.format(app)])

                if models:
                    base_model = getattr(models, 'Base')

                    for model in base_model.__subclasses__():
                        if model.__name__ not in used_models:
                            used_models.append(model.__name__)
                            AdminUtils.apps[app][model.__name__] = model
            except ImportError:
                continue