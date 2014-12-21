from tornado.web import authenticated
from core.web import RequestHandler
from .models import User
from .auth import Auth


class LoginHandler(RequestHandler, Auth):
    def get(self, *args, **kwargs):
        self.render('user/login.html')

    def post(self, *args, **kwargs):
        user = self.db.query(User).filter(
            User.name == self.get_argument('name', ''),
            User.password == self.get_argument('password', ''))

        if user.count() == 1:
            self.authorize(user.one())
            self.redirect(self.get_argument('next', self.reverse_url('index')))

        self.render('user/login.html')


class LogoutHandler(RequestHandler, Auth):
    @authenticated
    def get(self, *args, **kwargs):
        Auth.logout(self)
        self.redirect(self.get_argument('next', self.reverse_url('index')))