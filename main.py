#!/usr/bin/python3

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8000, help="run on the given port!", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self, op):
        # print("op:", op)
        greeting = self.get_argument("greeting", "Hello")
        self.write(greeting + ',friendly user!')


if __name__ == '__main__':
    if None:
        print("hello")
    else:
        print("wo")

    table_list = []
    for i in range(3,10):
        print(i)
        table_list.append("abc")
    print(table_list)
    table_list = ','.join(table_list)
    print(table_list)
    exit(1)

    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/?(test)", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
