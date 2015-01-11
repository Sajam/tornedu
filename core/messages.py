from types import MethodType
from .conf import Settings


class Messages(object):
    """
    Helper class to manage messages. Useful for example in RequestHandler (especially).
    In settings you can specify tuple of available types by setting MESSAGE_TYPES variable.

    To add new message just simply do (example):

        messages = Messages()
        messages.info('Hello, Developer!')
        messages.error('Unknown error occurred.')
    """
    def __init__(self):
        self.types = getattr(Settings, 'MESSAGE_TYPES', ('success', 'info', 'warning', 'error', ))
        self.messages = dict()

        self.initialize_types()

    def initialize_types(self):
        for type_name in self.types:
            self.messages[type_name] = []

            # Creating and binding class instance function with message type name.
            def func(cls, message_content, message_type=type_name):
                cls.append_message(message_type, message_content)

            setattr(self, type_name, MethodType(func, self))

    def append_message(self, message_type, message_content):
        self.messages[message_type].append(message_content)

    def add_many(self, message_type, messages):
        for message in messages:
            self.messages[message_type].append(message)

    def get_all(self):
        return self.messages

    def clear(self, type_name=None):
        if type_name:
            self.messages[type_name] = []
        else:
            self.messages = {type_name: [] for type_name in self.types}