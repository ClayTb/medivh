from tornado.web import RequestHandler


class route(object):

    def __init__(self, url):
        self.url = url

    def __call__(self, handler):

        pass


class BaseHandler(RequestHandler):
    pass


class MainHandler(BaseHandler):
    def get(self):
        self.write("Hello, world")
