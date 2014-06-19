# -*- coding: utf-8 -*-

__author__ = 'nothi'
import os
from tornado.web import  RequestHandler
from web.service.book_service import BookService
from web.settings import *

class ResultSetController(RequestHandler):
    def initialize(self):
        self.service = BookService()

    @staticmethod
    def __handler_action(action):
        if not action in ("any","title", "author", "isbn", "press"):
            return 'title'
        else:
            return action

    def get(self):
        #处理参数action
        action = self.get_argument("action")
        keyword = self.get_argument("keyword")
        index = self.get_argument("index",default=1)
        action = self.__handler_action(action)

        try:
            index = int(index)
        except Exception, e:
            index = 1

        #查询
        result = self.service.quey_by_keyword(action,keyword,(index  - 1) * ITEM_PER_PAGE,ITEM_PER_PAGE)

        #扩展模板
        if result == None or len(result) == 0:
            self.render(os.path.join(template_dir, "notfind.html"), sentence="哈哈，书没找到")
        else:
            self.render(os.path.join(template_dir, "resultset.html"),
                        keyword=keyword, action=action,
                        index=index,items=result, pagecount=self.service.get_page_size(action,keyword))
        print self.service.get_page_size(action,keyword)

    def post(self):
        self.get()


#测试
if __name__=="__main__":
    ser = BookService()
    list  = ser.__query_by_pair_any({"isbn":"00001001"})
    for a in list:
        print a

