from pprint import pprint
import math
import datetime
from .conf import Settings


def log(message=None, show_datetime=None, datetime_format=None, **kwargs):
    if not Settings.APP['debug']:
        return

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

