import os
from core.conf import Settings
from core.model import BaseModel
from core.database import Database
from core.utils import import_subclasses
from ..command import ManagementCommand


class ManagementCommandDatabase(ManagementCommand):
    command = ('db', 'database', )
    description = 'database management tools'

    def __init__(self, *args, **kwargs):
        super(ManagementCommandDatabase, self).__init__(*args, **kwargs)
        self.db = Database.instance().connect(Settings.DEFAULT_DATABASE_SETTINGS)

    @property
    def session(self):
        if not hasattr(self, '_session'):
            self._session = self.db.make_session()

        return self._session

    @ManagementCommand.action('drop_schema', 'drop')
    def drop_schema(self):
        ManagementCommandDatabase.import_models()
        BaseModel.metadata.drop_all(self.db.engine)

        print 'Database schema dropped successfully.'

    @ManagementCommand.action('create_schema', 'create')
    def create_schema(self):
        ManagementCommandDatabase.import_models()
        BaseModel.metadata.create_all(self.db.engine)

        print 'Database schema created successfully.'

    @ManagementCommand.action('import_data', 'data')
    def import_data(self):
        sql = open(os.path.join(Settings.BASE_PATH, 'misc/basic.sql'), mode='r').read()

        self.session.execute(sql)
        self.session.commit()

        print 'Data successfully imported.'

    @ManagementCommand.action('reset', 'recreate')
    def reset(self):
        self.drop_schema()
        self.create_schema()
        self.import_data()

        print 'Database reset finished successfully.'

    @staticmethod
    def import_models():
        import_subclasses(BaseModel, allowed_paths=Settings.LOADER_PATHS['models'], base_path=Settings.BASE_PATH)