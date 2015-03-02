#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, event
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from .utils import log


class Database(object):
    INITIALIZATION_INDICATOR = 'creating'
    queries = []

    @staticmethod
    def instance():
        if not hasattr(Database, '_instance'):
            Database._instance = Database.INITIALIZATION_INDICATOR
            Database()
            log('Database() instance created.')

        return Database._instance

    def __init__(self):
        instance = getattr(Database, '_instance') if hasattr(Database, '_instance') else None

        if not instance or (instance and instance != Database.INITIALIZATION_INDICATOR):
            raise Exception('Database object should be accessed using Database.instance() method.')
        elif instance == Database.INITIALIZATION_INDICATOR:
            self.session = sessionmaker()
            self.engine = None

            setattr(Database, '_instance', self)

    def connect(self, connection_settings):
        url = URL(
            connection_settings.get('driver', 'mysql'),
            **dict((k, connection_settings.get(k)) for k in ('username', 'password', 'host', 'port', 'database', 'query'))
        )

        print connection_settings.get('options', {})
        self.engine = create_engine(url, **connection_settings.get('options', {}))
        self.session.configure(bind=self.engine)

        event.listen(self.engine, 'before_cursor_execute', Database.log_query)
        log('Connected to database "{}" at {}{}.'.format(url.database, url.host, ':{}'.format(url.port) if url.port else ''))

        return self

    def make_session(self):
        Database.queries = []

        return self.session()

    @staticmethod
    def log_query(conn, cursor, statement, *args):
        Database.queries.append(statement)

    @staticmethod
    def get_queries():
        return Database.queries

    @staticmethod
    def queries_count():
        return len(Database.queries)