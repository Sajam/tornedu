from sqlalchemy.orm.exc import NoResultFound
from .models import User


class Auth(object):
    user_cookie_name = 'user'

    def authorize(self, user):
        self.set_secure_cookie(Auth.user_cookie_name, str(user.id))

    @staticmethod
    def get_current_user(request):
        # This method overriding Tornado's RequestHandler get_current_user() method (see __init__.py).
        user_cookie = request.get_secure_cookie(Auth.user_cookie_name)

        if user_cookie:
            if not request.current_user_cache:
                try:
                    request.current_user_cache = User.get(User.id == int(user_cookie))
                except NoResultFound:
                    Auth.logout(request)
                    request.redirect('index')

            return request.current_user_cache

    @staticmethod
    def logout(request):
        request.clear_cookie(Auth.user_cookie_name)