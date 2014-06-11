# -*- coding: utf-8 -*-
__author__ = 'nothi'

import json
from tornado.web import RequestHandler
from common.model.book_info import BookInfo
from web.service.book_service import BookService
from json import encoder
encoder.FLOAT_REPR = lambda o: format(o, '.2f')

def bookInfoToDict(book):
    result = {
        "name":book.title,
        "author":book.author,
        "originalPrice":float(book.price),
        "isbn":book.isbn,
        "press":book.press,
        "coverUrl":book.cover,
        "jdPrice":float(10),
        "ddPrice":float(10)
    }
    return result

class BookDetailController(RequestHandler):
    def initialize(self):
        self.service = BookService()

    def get(self,isbn):
        obj = self.service.query_by_pair_any({"isbn":isbn})
        if not obj:
            self.write("")
        else:
            result = bookInfoToDict(obj[0]);
            msg = json.dumps(result,ensure_ascii=False, encoding="utf-8")
            self.write(msg)

    def post(self,isbn):
        self.get(isbn)
