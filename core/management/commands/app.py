#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from core.conf import Settings
from ..command import ManagementCommand


class ManagementCommandApp(ManagementCommand):
    command = ('app', 'apps', )
    description = 'applications management'

    def __init__(self, *args, **kwargs):
        super(ManagementCommandApp, self).__init__(*args, **kwargs)

    @ManagementCommand.action('start', 'new')
    def start(self):
        if len(self.arguments) < 2:
            print 'Please specify application name.'
        else:
            app_name = self.arguments[1]
            app_path = os.path.join(Settings.BASE_PATH, 'apps/{}'.format(app_name))

            os.mkdir(app_path)

            for file_name, file_contents in self.files.iteritems():
                file = open(os.path.join('{}/{}'.format(app_path, file_name)), 'w+')
                file.write(file_contents.format(name=app_name, uname=app_name.title()))
                file.close()

            print 'App "{}" successfully created! To enable add it to Settings.APPS.'.format(app_name)

    @property
    def files(self):
        return {
            '__init__.py': '',

'urls.py':

"""#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado.web import URLSpec
from .handlers import {uname}Handler


URLS = [
    URLSpec(r'/{name}/handler/([0-9]+)$', {uname}Handler, name='{name}_handler'),
]""",


'models.py':

"""#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.model import *


class {uname}Model(BaseModel, TimestampMixin):
    __display_name__ = '{uname}'

    name = Column(String(length=255))

    def __repr__(self):
        return '<{uname}Model(id={{}}, name={{}})>'.format(self.id, self.name)""",


'handlers.py':

"""#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.web import RequestHandler
from .forms import {uname}Form


class {uname}Handler(RequestHandler):
    template = '{name}/view.html'

    def get(self):
        self.render(self.template, {name}_form={uname}Form())

    def post(self):
        self.render(self.template, {name}_form={uname}Form(self.request.body_arguments))""",


'forms.py':

"""#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.forms import *


class {uname}Form(Form):
    fields = [
        TextField('name', validators=[
            RequiredValidator
        ])
    ]

    labels = {{
        'name': 'Nazwa'
    }}"""
        }