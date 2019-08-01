import os
import logging

import tornado.ioloop
from tornado.web import Application
from tornado import autoreload


from orca.urls import urlpatterns
from settings import ORCA_DEVELOP_MODE, APPLICATION_CONFIG

logging.basicConfig(level=logging.INFO)


def make_app():
    return Application(urlpatterns, **APPLICATION_CONFIG)


if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    loop = tornado.ioloop.IOLoop.current()
    logging.info('==================Server Start==================')
    if ORCA_DEVELOP_MODE:
        logging.info(' -- develop mode')
        autoreload.start()
    else:
        logging.info(' -- production!!')
    loop.start()
