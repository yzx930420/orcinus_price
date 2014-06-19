# -*- coding: utf-8 -*-
__author__ = 'yzx930420'

from web import settings
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
        """
            返回页数
        """
        if action == 'any':
            action = 'title'
        page_count = 1;
        if action in ['title', 'isbn', 'author']:
            page_count = lucence_dao.get_page_size(action,keyword)
        page_count = (page_count + settings.ITEM_PER_PAGE - 1) /settings.ITEM_PER_PAGE
        return page_count

    def quey_by_isbn(self,isbn):
        book = book_dao.quey_by_isbn(isbn)
        if book:
            book.goods_list = book_dao.quey_by_isbn_for_goods(isbn)
        return book

    def quey_by_isbn_with_time(self, start, end):
        pass

# 测试
if __name__ == '__main__':
    book_service = BookService()
    for book in book_service.__query_by_pair_tail({'isbn':'0001'}):
        for goods in book.goods_list:
            print goods.isbn



