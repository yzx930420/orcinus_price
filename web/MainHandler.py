# -*- coding: utf-8 -*-
"""启动webtornado的入口 """
__author__ = 'nothi'

import os
import sys
from tornado.web import Application
from tornado.web import StaticFileHandler
from tornado.ioloop import IOLoop

workdir = os.path.split( os.path.realpath( sys.argv[0] ))[0]

settings = {
    "static_path": os.path.join(workdir, "static"),
    "listen_port":8888,
}


from web.controller import book_detail_controller,index_controller,result_set_controller

if __name__ == "__main__":
    application = Application([(r"/index", index_controller.IndexController),
        (r"/resultset", result_set_controller.ResultSetController),
        (r"/bookdetail/(.*)"), book_detail_controller.BookDetailController,
        (r"/static/(.*)", StaticFileHandler, dict(path=settings["static_path"])),])
    application.listen(settings["listen_port"])
    IOLoop.instance().start()



