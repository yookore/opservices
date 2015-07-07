import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

if 'PORT' in os.environ:
    print os.environ
    APP_PORT = os.environ['PORT']
else:
    print os.environ
    APP_PORT = 4443

define("port", default=APP_PORT, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
            (r"/hook-update", UpdateHookHandler)
        ]
        tornado.web.Application.__init__(self, handlers)


class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        print "Invoking BaseHandler"


class HomeHandler(BaseHandler):
    def get(self):
        self.write("Welcome to Git Hook Services")


class UpdateHookHandler(BaseHandler):
    def get(self):
        print "invoking UpdateHookHandler"

    def post(self):
        """ Retrieve the http post from github
        Check the commit for JIRA-styled issue key.
        if it's not there, reject the push and rollback the commit
        """
        ref = self.get_argument("ref")
        self.write(self.get_argument("commits"))
        print("Getting commits from ref %s " % ref)
        print(self.get_argument("commits"))


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
