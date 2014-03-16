# -*- coding: utf-8 -*-
__author__ = 'yzx930420'

from common.model.book import Book
from common.dao.book_dao import book_dao

class BookService(object):
    def query_by_pair_perfectly(self, pair):
        yield  book_dao.query_perfectly_matched(pair)

    def query_for_period_by_isbn(self, isbn, start_time, end_time):
        yield book_dao.query_by_time(isbn, start_time, end_time)

    def query_by_pair_any(self, pair):
        yield book_dao.query_any_matched(pair)

    def query_by_pair_front(self, pair):
        yield book_dao.query_front_matched(pair)

    def query_by_pair_tail(self, pair):
        yield book_dao.query_tail_matched(pair)

# 测试
if __name__ == '__main__':
    book_service = BookService()
    for book in book_service.query_by_keyword('50001'):
        print book



