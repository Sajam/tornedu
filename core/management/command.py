import types


class ManagementCommand(object):
    command = NotImplementedError()
    description = None

    def __init__(self, arguments, options):
        self.arguments = arguments
        self.options = options
        self.allowed_actions = self.collect_allowed_actions()

    def run(self):
        if self.check_arguments_valid():
            self.run_action()
        else:
            self.display_actions_help()

    def run_action(self):
        if self.arguments:
            action_function_handler = getattr(self, self.allowed_actions[self.arguments[0]].__name__)
            action_function_handler()

    def check_arguments_valid(self):
        return not self.allowed_actions or (
            self.allowed_actions and self.arguments and self.arguments[0] in self.allowed_actions
        )

    def display_actions_help(self):
        print 'Allowed actions:\n{}'.format(
            '\n'.join(['\t{}'.format(
                ', '.join(alias for alias in action.command) if isinstance(action.command, (list, tuple)) else
                action.command
            ) for action in set(self.allowed_actions.values())])
        )

    def collect_allowed_actions(self):
        allowed_actions = {}

        for k, v in self.__class__.__dict__.iteritems():
            if isinstance(v, types.FunctionType) and hasattr(v, 'is_action') and v.is_action:
                allowed_actions.update(
                    {alias: v for alias in v.command} if isinstance(v.command, (list, tuple)) else
                    {v.command: v}
                )

        return allowed_actions

    @staticmethod
    def action(*args, **kwargs):
        decorator_arguments = list(args)

        def decorate_action_function(function, command):
            function.is_action = True
            function.command = command

            return function

        if isinstance(decorator_arguments[0], types.FunctionType):
            return decorate_action_function(decorator_arguments[0], decorator_arguments[0].__name__)

        def wrapped(function, *args, **kwargs):
            return decorate_action_function(function, decorator_arguments)

        return wrapped