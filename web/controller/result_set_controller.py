# -*- coding: utf-8 -*-

__author__ = 'nothi'
import os
from tornado.web import  RequestHandler
from web.service.book_service import BookService
from web.settings import *

class ResultSetController(RequestHandler):
    def initialize(self):
        self.service = BookService()

    def get(self):
        action = self.get_argument("action")
        keyword = self.get_argument("keyword")
        result = []
        if action == None or action == "any":
           result = self.service.query_by_pair_any({'title'.encode('utf-8'):keyword.encode('utf-8')})
        else:
            result = self.service.query_by_pair_any({action.encode('utf-8'):keyword.encode('utf-8')})
            #result = self.service.query_by_pair({action:keyword})

        if result == None or len(result) == 0:
            self.render(os.path.join(template_dir, "notfind.html"), sentence="哈哈，书没找到")
        else:
            self.render(os.path.join(template_dir, "resultset.html"), list=result)

    def post(self):
        self.get()


#测试
if __name__=="__main__":
    ser = BookService()
    list  = ser.query_by_pair_any({"isbn":"00001001"})
    for a in list:
        print a

