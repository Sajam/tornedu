#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.utils import import_subclasses
from core.conf import Settings
from core.forms import *
from apps.category.models import Category
from .models import content_types


content_types_forms = {}


def content_type_form(content_type, *args, **kwargs):
    def wrapped(cls, *args, **kwargs):
        content_types_forms[content_type] = cls

        return cls

    return wrapped


class ContentForm(Form):
    fields = [
        SelectField(
            'type',
            blank='--- wybierz ---',
            options={
                content_type_name: content_type.__display_name__
                for content_type_name, content_type in content_types.iteritems()
            },
            validators=[
                RequiredValidator, InValidator(content_types.keys())
            ]
        ),
        SelectField('category', blank='--- wybierz ---', options=Category.tree_select_options, validators=[
            RequiredValidator
        ]),
        TextField('name', validators=[
            RequiredValidator, LengthValidator(min=3, max=255)
        ]),
        FileField('image')
    ]

    labels = {
        'type': 'Typ treści',
        'category': 'Kategoria',
        'name': 'Nazwa (tytuł) dla treści',
        'image': 'Obraz'
    }


import_subclasses(Form, allowed_paths=['apps.content.type.*.forms'], base_path=Settings.BASE_PATH)