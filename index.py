import tornado.web
import tornado.ioloop
from tornado.options import define,options
import request_handlers

import os


TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static")

if __name__ == "__main__":
    settings = dict(
            template_path = TEMPLATE_PATH,
            static_path = STATIC_PATH,
            debug = True,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            login_url = '/login/',
        )
    app =  tornado.web.Application([
        (r"/login/",request_handlers.LoginHandler),
        (r"/logout/",request_handlers.LogoutHandler)
        ], **settings)


    app.listen(8000)

    tornado.ioloop.IOLoop.current().start()
    