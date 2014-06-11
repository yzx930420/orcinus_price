# -*- coding: utf-8 -*-
__author__ = 'yzx930420'

from common.model.book import Book
from common.dao.book_dao import book_dao
from common.model.book_info import BookInfo
from common.model.book_goods_info import BookGoodsInfo

class BookService(object):
    def quey_by_keyword(self, action,  keyword, index, size):
        pass

    def query_by_pair_perfectly(self, pair):
        book_info_list = book_dao.query_perfectly_matched(pair)
        for book_info in book_info_list:
            book_info.goods_list = book_dao.query_to_get_book_goods_info_by_isbn(book_info.isbn)
        return book_info_list

    def query_by_pair_any(self, pair):
        book_info_list = book_dao.query_any_matched(pair)
        for book_info in book_info_list:
            book_info.goods_list = book_dao.query_to_get_book_goods_info_by_isbn(book_info.isbn)
        return book_info_list

    def query_by_pair_any_page(self, pair, page):
        """
           @pair :关键字
           @page: 页数
        """
        return self.query_by_pair_any(pair)[page * 10 : page * 10 + 10]

    def query_by_pair_size(self, pair):
        """
            返回有多少页
        """
        return len(self.query_by_pair_any(pair));

    def query_by_pair_front(self, pair):
        book_info_list = book_dao.query_front_matched(pair)
        for book_info in book_info_list:
            book_info.goods_list = book_dao.query_to_get_book_goods_info_by_isbn(book_info.isbn)
        return book_info_list

    def query_by_pair_tail(self, pair):
        book_info_list = book_dao.query_tail_matched(pair)
        for book_info in book_info_list:
            book_info.goods_list = book_dao.query_to_get_book_goods_info_by_isbn(book_info.isbn)
        return book_info_list

    def query_for_period_by_isbn(self, isbn, start_time, end_time):
        return book_dao.query_by_time(isbn, start_time, end_time)

# 测试
if __name__ == '__main__':
    book_service = BookService()
    for book in book_service.query_by_pair_tail({'isbn':'0001'}):
        for goods in book.goods_list:
            print goods.isbn



