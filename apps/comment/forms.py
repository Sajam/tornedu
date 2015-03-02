#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.forms import *


class CommentForm(Form):
    fields = [
        TextareaField('text', validators=[
            RequiredValidator
        ])
    ]

    labels = {
        'text': 'Treść'
    }