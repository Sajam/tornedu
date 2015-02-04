from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from core.conf import Settings


class Db(object):
    _instance = None
    queries = []

    @staticmethod
    def instance():
        if not Db._instance:
            Db._instance = Db()

        return Db._instance

    def __init__(self):
        self.session = sessionmaker()
        self.connection_name = None
        self.connection_settings = None
        self.engine = None

    def connect(self, database_connection_name):
        self.connection_name = database_connection_name
        self.connection_settings = Settings.DATABASES[database_connection_name]
        self.engine = create_engine(
            self.connection_settings['connection_string'],
            **self.connection_settings['kwargs']
        )
        self.session.configure(bind=self.engine)

        event.listen(self.engine, 'before_cursor_execute', Db.catch_queries)

        return self

    @staticmethod
    def catch_queries(conn, cursor, statement, *args):
        Db.queries.append(statement)

    @staticmethod
    def get_queries():
        return Db.queries

    @staticmethod
    def queries_count():
        return len(Db.queries)