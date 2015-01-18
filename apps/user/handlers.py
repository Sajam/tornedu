from tornado.web import authenticated
from core.web import RequestHandler
from .models import User
from .auth import Auth
from .forms import RegisterForm


class LoginHandler(RequestHandler, Auth):
    template = 'user/login.html'

    def post(self, *args, **kwargs):
        user = self.db.query(User).filter(User.name == self.get_argument('name', ''),
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


class RegisterHandler(RequestHandler):
    template = 'user/register.html'

    def get(self, *args, **kwargs):
        self.render(self.template, **{
            'register_form': RegisterForm()
        })

    def post(self, *args, **kwargs):
        form = RegisterForm(self.request.body_arguments)
        if form.validate():
            # Create user.
            pass
        else:
            self.messages.error(form.errors)

        self.render(self.template, **{
            'register_form': form
        })