import tornado.ioloop
import tornado.web
from controllers import MainHandler


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": "./css/"}),
    (r"/img/(.*)", tornado.web.StaticFileHandler, {"path": "./img/"}),
    (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": "./js/"})
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
