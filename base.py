from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    def get_current_user(self):
        user = self.get_secure_cookie("user")
        if not user:
            return
        else:
            return user.decode("utf-8")
