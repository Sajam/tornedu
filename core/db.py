from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.conf import Settings


class Db(object):
    _instance = None

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

        return self