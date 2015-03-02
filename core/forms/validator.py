#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .filters import Filters


class Validator(object):
    # In subclasses you can specify list of filters applied before validation.
    filters = []
    defined_filters = Filters.filters()

    def __init__(self, *args, **kwargs):
        self.args = args
        self.field = None
        self.form = None
        self.value = None
        self.errors_list = []

        for name, value in kwargs.iteritems():
            setattr(self, name, value)

    def prepare(self, field):
        self.field = field
        self.form = self.field.form
        self.value = self.field.value
        self.errors_list = []

        for filter in self.filters:
            self.value = self.defined_filters[filter](self.value)

        return self

    def validate_base(self):
        if not self.validate() and not len(self.errors_list):
            self.errors_list = [self.error]

        return not bool(len(self.errors_list))

    # Subclasses should implement this method and check if value is valid.
    def validate(self):
        raise NotImplementedError()

    # Subclasses can override this property to set default error message if validation fails.
    @property
    def error(self):
        return 'Field {} is not valid.'.format(self.field.name)

    @property
    def errors(self):
        return self.errors_list if len(self.errors_list) else False