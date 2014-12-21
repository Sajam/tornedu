#!/usr/bin/env python
import sys

if len(sys.argv) < 2:
    print 'Nothing to do.'
    exit()

action = sys.argv[1]

if action == 'create_schema':
    from core.conf import Settings
    from core.db import Db
    from core.model import *

    for app in Settings.APPS:
        try:
            __import__('apps.{}.models'.format(app), globals(), locals(), fromlist=['models'])
        except ImportError:
            pass

    Db.instance().connect('default')
    Base.metadata.create_all(Db.instance().engine)

    print 'Created database schema.'
else:
    print 'Action not supported.'

exit()