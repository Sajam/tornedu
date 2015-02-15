from core.conf import Settings
from core.model import BaseModel
from core.web import AdminRequestHandler


class AdminUtils(object):
    models_handlers = {}
    apps_models = {}
    models = {}
    model_to_app = {}

    def __init__(self):
        AdminUtils.get_apps_models()

    @staticmethod
    def get_apps_models():
        processed_models = []
        processed_admin_handlers = []

        for app_name in Settings.APPS:
            AdminUtils.apps_models[app_name] = {}

            try:
                models = __import__(
                    'apps.{}.models'.format(app_name),
                    fromlist=['apps.{}'.format(app_name)]
                )

                try:
                    admin_handlers = __import__(
                        'apps.{}.admin'.format(app_name),
                        fromlist=['apps.{}'.format(app_name)]
                    )

                    if admin_handlers:
                        for admin_handler in AdminRequestHandler.__subclasses__():
                            admin_handler_name = admin_handler.__name__

                            if admin_handler_name not in processed_admin_handlers:
                                processed_admin_handlers.append(admin_handler_name)

                                if hasattr(admin_handler, 'model'):
                                    model = getattr(admin_handler, 'model')
                                    AdminUtils.models_handlers[model.__name__] = admin_handler

                except ImportError:
                    pass

                if models:
                    for model in BaseModel.__subclasses__():
                        model_name = model.__name__

                        if model_name not in processed_models:
                            processed_models.append(model_name)

                            AdminUtils.apps_models[app_name][model_name] = model
                            AdminUtils.models[model_name] = model
                            AdminUtils.model_to_app[model_name] = app_name
            except ImportError:
                continue