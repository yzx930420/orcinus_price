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
        self.conn = MySQLdb.connect(common.dao.settings.MYSQL_URL,
                                    common.dao.settings.MYSQL_USER,
                                    common.dao.settings.MYSQL_PASSWORD,
                                    common.dao.settings.MYSQL_DATABASE)
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
        goods.crawling_time= book.crawling_time

        #step2 : book->bookpo
        bookpo = BookPO()
        bookpo.description = book.description
        bookpo.author = book.author
        bookpo.isbn = book.isbn
        bookpo.press = book.press
        bookpo.title = book.title
        bookpo.price = book.price
        return (goods, bookpo)

    def __parse_po_to_book(self, bookpo, goodspo):
        book = Book()

        # bookpo->book
        book['isbn'] = bookpo['isbn']
        book['price'] = bookpo['price']
        book['title'] = bookpo['title']
        book['author'] = bookpo['author']
        book['press'] = bookpo['press']
        book['description'] = bookpo['description']
        book['cover'] = bookpo['cover']

        #goodspo->book
        book['link'] = goodspo['link']
        book['platform'] = goodspo['platform']
        book['instant_price'] = goodspo['instant_price']
        book['crawling_time'] = goodspo['crawling_time']

        return book

    def insert(self, book):
        goods,bookpo = BookDAO.__parse_book_to_po(book)
        #插入goods(isbn, instant_price, link, platform, crawling_time)
        statement = 'insert into book_goods_info(isbn, instant_price, link, platform,crawling_time) values(%s, %s, %s, %s, %s)'
        self.cursor.execute(statement, [goods.isbn,goods.instant_price, goods.link, goods.platform, goods.crawling_time])
        self.cursor.commit()

    def query(self, pair):
        sql = 'select isbn, price, title, author, press, description, cover  from book_goods_info where %s=%s'
        self.cursor.execute(sql, pair)
        book=Book()
        bookpo_list = self.cursor.fetchall()
        booklist = []
        for bpo in bookpo_list:
            bookpo = BookPO()
            bookpo['isbn'] = bpo[0]
            bookpo['price'] = bpo[1]
            bookpo['title'] = bpo[2]
            bookpo['author'] = bpo[3]
            bookpo['press'] = bpo[4]
            bookpo['desciption'] = bpo[5]
            bookpo['cover'] = bpo[6]

            sql = 'select isbn, link, platform, instant_price, crawling_time from book_goods_info where %s=%s'
            self.cursor.execute(sql, ['isbn', bookpo['isbn']])
            goodspo_list = self.cursor.fetchall()
            for gpo in goodspo_list:
                goodspo = GoodsPO
                goodspo['isbn'] = gpo[0]
                goodspo['link'] = gpo[1]
                goodspo['platform'] = gpo[2]
                goodspo['instant_price'] = gpo[3]
                goodspo['crawling_time'] = gpo[4]
                booklist.append(self.__parse_po_to_book(bookpo, goodspo))

    def query(self, pair, start_time, end_time):
        pass

    def __del__(self):
        self.conn.close()

book_dao = BookDAO();

#测试
if __name__=="__main__":
    book = Book()
    book_dao.insert(book);
