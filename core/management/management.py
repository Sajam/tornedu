#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from core.conf import Settings
from core.utils import import_subclasses
from .command import ManagementCommand


class Management(object):
    def __init__(self, arguments):
        self.command, self.arguments, self.options = self.parse_arguments(arguments)
        self.management_commands = self.collect_management_commands()

        if self.check_arguments_valid():
            self.handle_options()
            self.display_management_environment_informations()
            self.run_command()
        else:
            self.display_commands_help()

        self.finalize()

    def handle_options(self):
        if 'settings' in self.options.keys() and self.options['settings']:
            os.environ['TORNADO_ENVIRONMENT_FORCE'] = self.options['settings']

            @Management.cleanup
            def cleanup():
                if 'TORNADO_ENVIRONMENT_FORCE' in os.environ:
                    del os.environ['TORNADO_ENVIRONMENT_FORCE']

    def display_management_environment_informations(self):
        print 'Using "{}" settings.'.format(Settings.ENVIRONMENT)

    def run_command(self):
        command = self.management_commands[self.command](self.arguments[1:], self.options)
        command.run()

    def check_arguments_valid(self):
        return self.command and self.command in self.management_commands.keys()

    def display_commands_help(self):
        print 'Available commands:\n{}'.format(
            '\n'.join([
                '\t{}{}'.format(
                    ', '.join(alias for alias in command.command) if isinstance(command.command, (list, tuple)) else
                    command.command,
                    ' - {}'.format(command.description) if command.description else ''
                ) for command in set(self.management_commands.itervalues())
            ])
        )

    def finalize(self):
        if hasattr(Management, 'cleanup_functions'):
            for cleanup_function in Management.cleanup_functions:
                cleanup_function()

    @staticmethod
    def parse_arguments(raw_arguments):
        arguments = []
        options = {}

        for argument in raw_arguments:
            if argument.startswith('--'):
                option_name, option_value = argument[2:].split('=', 1) if '=' in argument else [argument[2:], None]
                options[option_name] = option_value
            else:
                arguments.append(argument)

        return arguments[0] if arguments else None, arguments, options

    @staticmethod
    def collect_management_commands():
        management_commands = {}
        management_classes = import_subclasses(
            ManagementCommand,
            allowed_paths=Settings.LOADER_PATHS['management'],
            base_path=Settings.BASE_PATH
        )

        for command in management_classes:
            if isinstance(command.command, NotImplementedError):
                raise Exception('Management command class "{}" has no command attribute specified.'
                                .format(command.__name__))

            management_commands.update(
                {alias: command for alias in command.command} if isinstance(command.command, (tuple, list)) else
                {command.command: command}
            )

        return management_commands

    @staticmethod
    def cleanup(function):
        if not hasattr(Management, 'cleanup_functions'):
            Management.cleanup_functions = []

        Management.cleanup_functions.append(function)

        return function