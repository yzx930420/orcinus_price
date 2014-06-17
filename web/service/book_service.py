# -*- coding: utf-8 -*-
__author__ = 'yzx930420'

from common.model.book import Book
from common.dao.book_dao import book_dao
from common.dao.lucence_dao import lucence_dao
from common.model.book_info import BookInfo
from common.model.book_goods_info import BookGoodsInfo

class BookService(object):
    def quey_by_keyword(self, action,  keyword, index, size):
        """
            通过关键字和关键字的类型查询
            @parms: action:查询的类型有四种，(title, isbn, author, any)
                    keyword:关键字
                    index:起始点
                    size:个数
            @return:book_info的列表
        """
        #step 1: 处理action
        if not action in ["title", 'isbn', 'author']:
            action = 'title'
        #step 2: 得到isbn列表
        if action != 'isbn':
            isbns = lucence_dao.query(action, keyword, index, size)
        else:
            isbns = [keyword]
        #step 3: 获取book_info
        books = []
        for isbn in isbns:
            book = book_dao.quey_by_isbn(isbn)
            if book:
                books.append(book)
        return books

    def get_page_size(self, action, keyword):
        if action in ['title', 'isbn', 'author']:
            lucence_dao.get_page_size(action,keyword)
        else:
            return 1

    def quey_by_isbn(self,isbn):
        result = self.__query_by_pair_any({"isbn":isbn})
        return result[0] if result else None

    def quey_by_isbn_with_time(self, start, end):
        pass

    def query_by_pair_any_page(self, pair, page):
        """
           @pair :关键字
           @page: 页数
        """
        return self.__query_by_pair_any(pair)[page * 10 : page * 10 + 10]

    def query_by_pair_size(self, pair):
        """
            返回有多少页
        """
        return len(self.__query_by_pair_any(pair));


    def __query_by_pair_perfectly(self, pair):
        book_info_list = book_dao.query_perfectly_matched(pair)
        for book_info in book_info_list:
            book_info.goods_list = book_dao.query_to_get_book_goods_info_by_isbn(book_info.isbn)
        return book_info_list


    def __query_by_pair_any(self, pair):
        book_info_list = book_dao.query_any_matched(pair)
        for book_info in book_info_list:
            book_info.goods_list = book_dao.query_to_get_book_goods_info_by_isbn(book_info.isbn)
        return book_info_list

    def __query_by_pair_front(self, pair):
        book_info_list = book_dao.query_front_matched(pair)
        for book_info in book_info_list:
            book_info.goods_list = book_dao.query_to_get_book_goods_info_by_isbn(book_info.isbn)
        return book_info_list

    def __query_by_pair_tail(self, pair):
        book_info_list = book_dao.query_tail_matched(pair)
        for book_info in book_info_list:
            book_info.goods_list = book_dao.query_to_get_book_goods_info_by_isbn(book_info.isbn)
        return book_info_list

    def __query_for_period_by_isbn(self, isbn, start_time, end_time):
        return book_dao.query_by_time(isbn, start_time, end_time)

# 测试
if __name__ == '__main__':
    book_service = BookService()
    for book in book_service.__query_by_pair_tail({'isbn':'0001'}):
        for goods in book.goods_list:
            print goods.isbn



