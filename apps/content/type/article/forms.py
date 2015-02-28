#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.forms import *
from ...forms import content_type_form


@content_type_form('article')
class ContentTypeArticleForm(Form):
    fields = [
        TextField('content', validators=[
            RequiredValidator, LengthValidator(min=10)
        ]),
    ]

    labels = {
        'content': 'Treść',
    }