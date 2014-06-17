# -*- coding: utf-8 -*-
__author__ = 'nothi'

from tornado.web import RequestHandler
from web.service.book_service import BookService
from common.model.book_info import BookInfo
from web import  settings
import json
from json import encoder
encoder.FLOAT_REPR = lambda o: format(o, '.2f')


def bookInfoToDict(book):
    result = {
        "name":book.title,
        "author":book.author,
        "price":float(book.price),
        "isbn":book.isbn,
        "press":book.press,
        "coverUrl":book.cover
    }
    return result

class ResultSetController(RequestHandler):
    def initialize(self):
        self.service = BookService()

    def get(self):
        action = self.get_argument("action", default="any")
        keyword = self.get_argument("keyword")
        books = self.service.quey_by_keyword(action, keyword, 1, settings.MAX_SIZE_EACH_SIZE)
        jsons = []
        for book in books:
            jsons.append(bookInfoToDict(book))
        self.write(json.dumps(jsons,ensure_ascii=False))

    def post(self):
        self.get();
