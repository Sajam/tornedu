#!/usr/bin/env python
import sys

if len(sys.argv) < 2:
    print 'Nothing to do.'
    exit()

action = sys.argv[1]

if action == 'create_schema':
    from core.conf import Settings
    from core.database import Database
    from core.model import *

    Database.connect('default')
    db_engine = Database.engine

    for app in Settings.APPS:
        try:
            __import__('apps.{}.models'.format(app), globals(), locals(), fromlist=['models'])
        except ImportError:
            pass

    BaseModel.metadata.drop_all(db_engine)
    BaseModel.metadata.create_all(db_engine)

    print 'Created database schema.'
else:
    print 'Action not supported.'

exit()