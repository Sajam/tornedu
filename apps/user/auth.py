from sqlalchemy.orm.exc import NoResultFound
from .models import User


# Auth should extends request handlers (login/logout handlers).
class Auth(object):
    user_cookie_name = 'user'

    def authorize(self, user):
        self.set_secure_cookie(Auth.user_cookie_name, str(user.id))

    def logout(self):
        self.clear_cookie(Auth.user_cookie_name)

    # This method overriding Tornado's RequestHandler get_current_user() method (see __init__.py).
    @staticmethod
    def get_current_user(request):
        user_cookie = request.get_secure_cookie(Auth.user_cookie_name)

        if user_cookie:
            try:
                return User.get(User.id == int(user_cookie))
            except NoResultFound:
                request.logout()
                request.redirect('index')