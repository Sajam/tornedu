from core.conf import Settings
from core.model import Base


class AdminUtils(object):
    apps_models = {}
    models = {}
    model_to_app = {}

    def __init__(self):
        AdminUtils.get_apps_models()

    @staticmethod
    def get_apps_models():
        processed_models = []

        for app_name in Settings.APPS:
            AdminUtils.apps_models[app_name] = {}

            try:
                models = __import__(
                    'apps.{}.models'.format(app_name),
                    fromlist=['apps.{}'.format(app_name)]
                )

                if models:
                    for model in Base.__subclasses__():
                        model_name = model.__name__

                        if model_name not in processed_models:
                            processed_models.append(model_name)

                            AdminUtils.apps_models[app_name][model_name] = model
                            AdminUtils.models[model_name] = model
                            AdminUtils.model_to_app[model_name] = app_name
            except ImportError:
                continue