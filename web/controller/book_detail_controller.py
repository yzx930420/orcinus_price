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

    @staticmethod
    def get_platfrom_name(platform):
        platfom_name = {
            0:"当当网",
            1:"京东商城",
            2:"亚马逊"
        }
        return platfom_name[platform]

    def get(self, isbn):
        result = self.service.quey_by_isbn(isbn)

        if  result:
            for goods_info in result.goods_list:
                goods_info.platform = self.get_platfrom_name(goods_info.platform)
            comments = self.comment_service.get_comment(isbn)
            self.render(os.path.join(template_dir, "bookdetail.html"), book=result,comments=comments)
        else:
            self.render(os.path.join(template_dir, "notfind.html"), sentence="哈哈，书没找到")

    def post(self, isbn):
        self.get()
