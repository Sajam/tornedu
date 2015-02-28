import os
import math
import copy
import datetime
from pprint import pprint


def log(message=None, show_datetime=None, datetime_format=None, **kwargs):
    width = 80

    if show_datetime is None:
        show_datetime = True

    if show_datetime:
        date_result = datetime.datetime.now().strftime(datetime_format or '%H:%M:%S.%f')

        if message:
            message = '{} :: {}'.format(date_result, message)
        else:
            message = date_result

    if 'data' in kwargs:
        message = ' {} '.format(message) if message else ''
        line_characters_left = width - len(message)

        if line_characters_left > 0:
            message = '{}{}{}'.format('-' * int(line_characters_left // 2), message,
                                      '-' * int(math.ceil(line_characters_left / 2)))

        print(message)
        pprint(kwargs['data'], indent=4, width=width)
        print('-' * width)
    else:
        print(message)


def all_subclasses(cls):
    return cls.__subclasses__() + [g for s in cls.__subclasses__() for g in all_subclasses(s)]


def import_subclasses(cls, allowed_paths=None, base_path=None):
    allowed_paths = copy.deepcopy(allowed_paths) or ['*']
    base_path = base_path or '/'
    matching_allowed = []

    for path in allowed_paths:
        allowed_paths[allowed_paths.index(path)] = path.split('.')

    for root, dirs, files in os.walk(base_path):
        for name in files:
            path = os.path.join(root, name).replace(base_path, '').strip('./').rsplit('.', 1)[0]
            path_parts = path.split('/')

            for allowed_path in allowed_paths:
                matching = True

                for i, path_part in enumerate(path_parts):
                    if i > len(allowed_path) - 1 or (allowed_path[i] != '*' and allowed_path[i] != path_part)\
                            or len(path_parts) != len(allowed_path):
                        matching = False
                        break

                if matching and path not in matching_allowed:
                    matching_allowed.append(path.replace('/', '.'))

    for module_path in matching_allowed:
        __import__(module_path)

    return all_subclasses(cls)


def import_class_from_path(class_name, path=None):
    try:
        return __import__('.'.join(([path] if path else []) + [class_name]), globals(), locals(), fromlist=[class_name])
    except ImportError:
        pass


def directories_in_path(path):
    return next(os.walk(path))[1]