# -*- coding: utf-8 -*-
__author__ = 'yzx930420'

from common.model.book import Book
from common.dao.book_dao import book_dao

class BookService(object):
    def query_by_keyword(self, keyword):
        for attr in Book.attrs:
            if attr == 'time':
                continue
            for book in book_dao.query_perfectly_matched({attr: keyword}):
                yield book

    def query_by_pair(self, pair):
        yield  book_dao.query_perfectly_matched(pair)

    def query_for_period(self, isbn, start_time, end_time):
        yield book_dao.query_by_time(isbn, start_time, end_time)

# 测试
if __name__ == '__main__':
    book_service = BookService()
    for book in book_service.query_by_keyword('50001'):
        print book



