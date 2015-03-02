#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Filters(object):
    @staticmethod
    def strip(value):
        return value.strip()

    @staticmethod
    def filters():
        return {
            filter_name: getattr(Filters, filter_name)
            for filter_name in dir(Filters)
            if not filter_name.startswith('_') and filter_name not in ('filters', )
        }