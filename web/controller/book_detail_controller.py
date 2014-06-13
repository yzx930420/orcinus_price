# -*- coding: utf-8 -*-

__author__ = 'nothi'

from os.path import join
from tornado.web import RequestHandler
from web.service.book_service import BookService
from web.service.comment_service import CommentService
from web.settings import *

class BookDetailController(RequestHandler):
    def initialize(self):
        self.service = BookService()
        self.comment_service = CommentService()

    def get(self, isbn):
        result = self.service.quey_by_isbn(isbn)
        if  result:
            for goods_info in result.goods_list:
                if goods_info.platform == 0:
                    goods_info.platform = '当当网'
                elif goods_info.platform == 1:
                    goods_info.platform = '京东商城'
                elif goods_info.platform == 2:
                    goods_info.platform = '亚马逊'

            comments = self.comment_service.get_comment(isbn)
            self.render(os.path.join(template_dir, "bookdetail.html"), book=result,comments=comments)
        else:
            self.render(os.path.join(template_dir, "notfind.html"), sentence="哈哈，书没找到")

    def post(self, isbn):
        self.get()
