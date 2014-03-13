__author__ = 'yzx930420'

from common.model.book import Book
from common.dao.book_dao import book_dao

class BookService(object):
    def query_by_keyword(self, keyword):
        for attr in Book.attrs:
            if attr == 'time':
                continue
            print attr
            yield book_dao.query({attr, keyword})

    def query_by_pair(self, pair):
        yield  book_dao.query(pair)


    def query_for_period(self, isbn, start_time, end_time):
        yield book_dao.query({'isbn', isbn}, start_time, end_time)

