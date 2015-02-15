from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from core.conf import Settings
from core.database import Database
from core.utils import log

if __name__ == '__main__':
    app = Application(Settings.URLS, **Settings.APP)

    server = HTTPServer(app)
    server.bind(Settings.PORT)
    server.start(Settings.THREADS)

    Database.connect(Settings.DATABASE)

    log("Server started - access at http://127.0.0.1:{}/".format(Settings.PORT))

    IOLoop.current().start()