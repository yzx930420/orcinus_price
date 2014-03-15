# -*- coding: utf-8 -*-
"""这里实现了对MYSQL的简单操作(同步的，阻塞的). """
__author__ = 'yzx930420'

import MySQLdb
import common.dao.settings
from common.model.book import Book
from common.model.book_goods_info import BookGoodsInfo as GoodsPO
from common.model.book_info import BookInfo as  BookPO


class BookDAO():
    def __init__(self):
        self.conn = MySQLdb.connect(MYSQL_URL, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE)
        self.cursor = self.conn.cursor()

    def __parse_book_to_po(book_1):
        #把Book转化为两个PO实体
        book = Book()
        #steop1 : book->goods
        goods = GoodsPO()
        goods.isbn = book.isbn
        goods.instant_price = book.instant_price
        goods.link = book.instant_price
        goods.platform = book.platform
        goods.time = book.time

        #step2 : book->bookpo
        bookpo = BookPO()
        bookpo.desc = book.desc
        bookpo.author = book.author
        bookpo.isbn = book.isbn
        bookpo.press = book.press
        bookpo.title = book.title
        bookpo.price = book.price
        return (goods, bookpo)


    def insert(self, book):
        goods,bookpo = BookDAO.__parse_book_to_po(book)
        #插入goods(isbn, instant_price, link, platform, time)
        statement = 'insert into book_goods_info(isbn, instant_price, link, platform,time) values(%s, %s, %s, %s, %s)'
        self.cursor.execute(statement, [goods.isbn,goods.instant_price, goods.link, goods.platform, goods.time])
        self.cursor.commit()

    def query(self, map):
        pass

    def query(self, map, start_time, end_time):
        pass

    def __del__(self):
        self.conn.close()

book_dao = BookDAO();

#测试
if __name__=="__main__":
    book = Book()
    book_dao.insert(book);
