#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.forms import *
from ...forms import content_type_form
from .providers import VideoProvider


@content_type_form('video')
class ContentTypeVideoForm(Form):
    fields = [
        SelectField(
            'provider',
            options={id: provider.name for id, provider in VideoProvider.get_types().iteritems()},
            validators=[
                RequiredValidator
            ]
        ),
        TextField('content', validators=[
            RequiredValidator
        ]),
        TextField('duration', initial_value='00:00:00', validators=[
            RegexValidator(regex='^[0-9]{2}:[0-9]{2}:[0-9]{2}$')
        ]),
    ]

    labels = {
        'provider': 'Dostawca/źródło filmu',
        'content': 'URL filmu lub kod embed dla typu "Domyślny"',
        'duration': 'Długość filmu (GG:MM:SS)',
    }