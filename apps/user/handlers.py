from core.web import RequestHandler
from .models import User


class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('user/login.html')

    def post(self, *args, **kwargs):
        user = self.db.query(User).filter(
            User.name == self.get_argument('name', ''),
            User.password == self.get_argument('password', ''))

        if user.count() == 1:
            user.one().login()

        self.render('user/login.html')