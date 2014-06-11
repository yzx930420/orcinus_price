# -*- coding: utf-8 -*-
"""启动webtornado的入口 """
__author__ = 'nothi'

import os
import sys
from tornado.web import Application
from tornado.web import StaticFileHandler
from tornado.ioloop import IOLoop
from web.settings import *
#
# workdir = os.path.split( os.path.realpath( sys.argv[0] ))[0]
#
# settings = {
#     "static_path": os.path.join(workdir, "static"),
#     "template_path": os.path.join(workdir, "template"),
#     "listen_port":8888,
#     "xsrf_cookies": False,
#
# }



from web.controller import book_detail_controller,index_controller,result_set_controller
from web.controller.json import comment_detail_controller as json_comment
from web.controller.json import result_set_controller as json_result
from web.controller.json import book_detail_controller as json_book

if __name__ == "__main__":
    print workdir
    application = Application([(r"/index", index_controller.IndexController),
        (r"/", index_controller.IndexController),
        (r"/resultset", result_set_controller.ResultSetController),
        (r"/bookdetail/(.*)", book_detail_controller.BookDetailController),
        (r"/json/comment/(.*)", json_comment.CommentDetailController),
        (r"/json/book/(.*)", json_book.BookDetailController),
        (r"/json/resultset", json_result.ResultSetController),
        (r"/static/(.*)", StaticFileHandler, dict(path=settings["static_path"])),])
    application.listen(settings["listen_port"])
    IOLoop.instance().start()



