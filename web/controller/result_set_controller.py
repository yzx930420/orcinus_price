# -*- coding: utf-8 -*-

__author__ = 'nothi'
import os
from tornado.web import  RequestHandler
from web.service.book_service import BookService
from web.settings import *

ITEM_PER_PAGE = 15
class ResultSetController(RequestHandler):
    def initialize(self):
        self.service = BookService()

    def get(self):
        action = self.get_argument("action")
        if not action in ("any","title", "author", "isbn", "press"):
            action = any
        keyword = self.get_argument("keyword")
        index = int(self.get_argument("index",default=1))
        result = self.service.quey_by_keyword(action,keyword,(index  - 1) * ITEM_PER_PAGE,ITEM_PER_PAGE)
        item = result[0].goods_list if result else []

        if result == None or len(result) == 0:
            self.render(os.path.join(template_dir, "notfind.html"), sentence="哈哈，书没找到")
        else:
            self.render(os.path.join(template_dir, "resultset.html"),
                        keyword=keyword, action=action,
                        index=index,items=result, pagecount=self.service.get_page_size(action,keyword))

    def post(self):
        self.get()


#测试
if __name__=="__main__":
    ser = BookService()
    list  = ser.__query_by_pair_any({"isbn":"00001001"})
    for a in list:
        print a

