#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.forms import *


class LearnForm(Form):
    fields = [
        TextField('name', validators=[
            RequiredValidator
        ])
    ]

    labels = {
        'name': 'Nazwa'
    }