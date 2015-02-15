from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from .conf import Settings
from .utils import log


class Database(object):
    queries = []
    creating_indicator = 'creating'

    @staticmethod
    def instance():
        if not hasattr(Database, '_instance'):
            Database._instance = Database.creating_indicator
            Database._instance = Database()

        return Database._instance

    def __init__(self):
        if not hasattr(Database, '_instance') or (
                hasattr(Database, '_instance') and Database._instance != Database.creating_indicator):
            raise Exception('Database object should be accessed using Database.instance() method.')

        self.session = sessionmaker()
        self.engine = None

        log('Created Database() instance')

    def connect(self, connection_name):
        connection_settings = Settings.DATABASES[connection_name]

        self.engine = create_engine(connection_settings['connection_string'], **connection_settings['kwargs'])
        self.session.configure(bind=self.engine)

        event.listen(self.engine, 'before_cursor_execute', Database.catch_queries)

        log('Connected to database "{}"'.format(connection_name))

        return self

    def make_session(self):
        Database.queries = []

        return self.session()

    @staticmethod
    def catch_queries(conn, cursor, statement, *args):
        Database.queries.append(statement)

    @staticmethod
    def get_queries():
        return Database.queries

    @staticmethod
    def queries_count():
        return len(Database.queries)


# Immediately create Database() instance.
Database = Database.instance()