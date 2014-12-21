from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from core.conf import Settings


if __name__ == '__main__':
    app = Application(Settings.URLS, **Settings.APP)

    server = HTTPServer(app)
    server.bind(Settings.PORT)
    server.start(Settings.THREADS)

    IOLoop.current().start()