# -*- coding: utf-8 -*-
__author__ = 'nothi'

import json
from web import settings
from tornado.web import RequestHandler
from common.model.book_info import BookInfo
from common.model.book_goods_info import BookGoodsInfo
from web.service.book_service import BookService
from json import encoder
encoder.FLOAT_REPR = lambda o: format(o, '.2f')

def getJDPrice(book):
    for goods in  book.goods_list:
        if goods.platform == 1:
            return goods.instant_price
    return -1

def getDDPrice(book):
    for goods in  book.goods_list:
        if goods.platform == 0:
            return goods.instant_price
    return -1

def filter(book):
    price1 = getJDPrice(book)
    price2 = getDDPrice(book)
    price = price1 if price1 != -1 else price2
    return price


def bookInfoToDict(book):
    result = {
        "name":book.title,
        "author":book.author,
        "originalPrice":float(book.price),
        "isbn":book.isbn,
        "press":book.press,
        "coverUrl":book.cover,
        "jdPrice":float( filter(getJDPrice(book)) ),
        "ddPrice":float( filter(getDDPrice(book)) )
    }
    return result

class BookDetailController(RequestHandler):
    def initialize(self):
        self.service = BookService()

    def get(self,isbn):
        obj = self.service.quey_by_isbn(isbn)
        if not obj:
            self.write("")
        else:
            result = bookInfoToDict(obj[0]);
            msg = json.dumps(result,ensure_ascii=False, encoding="utf-8")
            self.write(msg)

    def post(self,isbn):
        self.get(isbn)
