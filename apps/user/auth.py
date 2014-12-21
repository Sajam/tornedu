import pickle


class Auth(object):
    user_cookie_name = 'user'

    def authorize(self, user):
        self.set_secure_cookie(Auth.user_cookie_name, pickle.dumps(user))

    @staticmethod
    def get_current_user(request):
        user_cookie = request.get_secure_cookie(Auth.user_cookie_name)
        if user_cookie:
            return pickle.loads(user_cookie)

        return False

    @staticmethod
    def logout(request):
        request.clear_cookie(Auth.user_cookie_name)