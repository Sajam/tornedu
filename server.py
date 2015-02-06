from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from core.conf import Settings
from core.db import Db

if __name__ == '__main__':
    app = Application(Settings.URLS, **Settings.APP)

    server = HTTPServer(app)
    server.bind(Settings.PORT)
    server.start(Settings.THREADS)

    Db.connect(Settings.DATABASE)

    IOLoop.current().start()