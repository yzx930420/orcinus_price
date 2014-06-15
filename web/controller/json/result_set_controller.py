# -*- coding: utf-8 -*-
__author__ = 'nothi'

from tornado.web import RequestHandler
from web.service.book_service import BookService
from common.model.book_info import BookInfo
import json
from json import encoder
encoder.FLOAT_REPR = lambda o: format(o, '.2f')


MAX_BOOK_AMOUNT = 40
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
        books = self.service.__query_by_pair_any({"title":keyword})
        jsons = []
        i = 0
        for book in books:
            jsons.append(bookInfoToDict(book))
            i = i + 1
            if i > MAX_BOOK_AMOUNT:
                break
        self.write(json.dumps(jsons,ensure_ascii=False))

    def post(self):
        self.get();
