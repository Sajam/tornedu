#!/usr/bin/env python
import sys

if len(sys.argv) < 2:
    print 'Nothing to do.'
    exit()

action = sys.argv[1]

if action == 'create_schema':
    from core.conf import Settings
    from core.database import Db
    from core.model import *

    db = Db.instance()
    db.connect('default')
    db_engine = Db.instance().engine

    for app in Settings.APPS:
        try:
            __import__('apps.{}.models'.format(app), globals(), locals(), fromlist=['models'])
        except ImportError:
            pass

    Base.metadata.drop_all(db_engine)
    Base.metadata.create_all(db_engine)

    print 'Created database schema.'
else:
    print 'Action not supported.'

exit()