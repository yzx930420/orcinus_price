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
        self.conn = MySQLdb.connect(host=common.dao.settings.MYSQL_URL,
                                    user=common.dao.settings.MYSQL_USER,
                                    passwd=common.dao.settings.MYSQL_PASSWORD,
                                    db=common.dao.settings.MYSQL_DATABASE)
        self.cursor = self.conn.cursor()

    def __parse_book_to_po(self, book):
        #把Book转化为两个PO实体
        #steop1 : book->goods
        goods = GoodsPO()
        goods.isbn = book.isbn
        goods.instant_price = book.instant_price
        goods.link = book.link
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
        bookpo.cover = book.cover
        return (goods, bookpo)

    def __parse_po_to_book(self, bookpo, goodspo):
        book = Book()

        # bookpo->book
        book.isbn = bookpo.isbn
        book.price = bookpo.price
        book.title = bookpo.title
        book.author = bookpo.author
        book.press = bookpo.press
        book.description = bookpo.description
        book.cover = bookpo.cover

        #goodspo->book
        book.link = goodspo.link
        book.platform = goodspo.platform
        book.instant_price = goodspo.instant_price
        book.crawling_time = goodspo.crawling_time

        return book

    # 插入book
    def insert(self, book):
        goods,bookpo = self.__parse_book_to_po(book)
        # 插入goods(isbn, instant_price, link, platform, crawling_time)
        statement = 'insert into book_goods_info(isbn, instant_price, link, platform,crawling_time) ' \
                    'values(%s, %s, %s, %s, %s)'

        self.cursor.execute(statement, [goods.isbn,
                                        goods.instant_price,
                                        goods.link,
                                        goods.platform,
                                        goods.crawling_time
        ])

        # 判断book_info中是否已经存在
        select_sql = 'select * from book_info where isbn = %s' %(bookpo.isbn)
        print 'sql = ', select_sql
        self.cursor.execute(select_sql)
        len = self.cursor.fetchall().__len__()
        print 'cover = ', bookpo.cover
        if  len == 0:
            statement_book_info = \
                "insert into book_info(isbn, price, title, author, press, description, cover) " \
                "values(%s,%s,%s,%s,%s,%s,%s)"

            self.cursor.execute(statement_book_info, [bookpo.isbn,
                                                      bookpo.price,
                                                      bookpo.title,
                                                      bookpo.author,
                                                      bookpo.press,
                                                      bookpo.description,
                                                      bookpo.cover])
        self.conn.commit()

    # 对键值对pair进行查询，完全匹配, return bookpo_list
    def query_perfectly_matched(self, pair):
        key = MySQLdb.escape_string(pair.keys()[0])
        value = MySQLdb.escape_string(pair[key])
        sql = 'select isbn, price, title, author, press, description, cover ' \
              'from book_info ' \
              'where %s="%s"' %(key, value)
        self.cursor.execute(sql)
        result_list = self.cursor.fetchall()
        bookpo_list = []
        for result in result_list:
            bookpo = BookPO()
            bookpo.set_all(result)
            bookpo_list.append(bookpo)

        return bookpo_list

    # 对键值对pair进行查询，任意匹配
    def query_any_matched(self, pair):
        key = MySQLdb.escape_string(pair.keys()[0])
        value = MySQLdb.escape_string(pair[key])
        sql = 'select isbn, price, title, author, press, description, cover ' \
              'from book_info ' \
              'where %s like "%%%s%%"' %(key, value)
        self.cursor.execute(sql)
        result_list = self.cursor.fetchall()
        bookpo_list = []
        for result in result_list:
            bookpo = BookPO()
            bookpo.set_all(result)
            bookpo_list.append(bookpo)

        return bookpo_list

    # 对键值对pair进行查询，前方匹配
    def query_front_matched(self, pair):
        key = MySQLdb.escape_string(pair.keys()[0])
        value = MySQLdb.escape_string(pair[key])
        sql = 'select book_info.isbn, price, title, author, press, description, cover ' \
              'from book_info ' \
              'where %s like "%s%%" '%(key, value)
        self.cursor.execute(sql)
        result_list = self.cursor.fetchall()
        bookpo_list = []
        for result in result_list:
            bookpo = BookPO()
            bookpo.set_all(result)
            bookpo_list.append(bookpo)

        return bookpo_list

    # 对键值对pair进行查询，尾部匹配
    def query_tail_matched(self, pair):
        key = MySQLdb.escape_string(pair.keys()[0])
        value = MySQLdb.escape_string(pair[key])
        sql = 'select isbn, price, title, author, press, description, cover ' \
              'from book_info ' \
              'where %s like "%%%s"' %(key, value)
        self.cursor.execute(sql)
        result_list = self.cursor.fetchall()
        bookpo_list = []
        for result in result_list:
            bookpo = BookPO()
            bookpo.set_all(result)
            bookpo_list.append(bookpo)

        return bookpo_list

    # 传入isbn通过时间范围查询
    def query_by_time(self, isbn, start_time, end_time):
        sql = 'select book_info.isbn, price, title, author, press, description, cover, ' \
              'link, platform, instant_price, crawling_time ' \
              'from book_info, book_goods_info ' \
              'where book_info.isbn = book_goods_info.isbn and book_info.isbn="%s" ' \
              'and crawling_time between %d and %d' %(isbn, start_time, end_time)
        self.cursor.execute(sql)
        result_list = self.cursor.fetchall()
        book_list = []
        for result in result_list:
            book = Book()
            book.set_all(result)
            book_list.append(book)

        return book_list

    def query_to_get_book_goods_info_by_isbn(self, isbn):
        sql = 'select isbn, link, platform, instant_price, max(crawling_time) ' \
              'from book_goods_info ' \
              'where isbn="%s" ' \
              'group by platform' %(isbn)
        self.cursor.execute(sql)
        result_list = self.cursor.fetchall()
        goods_list = []
        for result in result_list:
            goodspo = GoodsPO()
            goodspo.set_all(result)
            goods_list.append(goodspo)

        return goods_list

    def __del__(self):
        self.conn.close()

book_dao = BookDAO()

#测试
def test_insert():
    for i in range(1,101):
        book = Book()
        index = (i+1) / 2
        book.isbn = '%05d001'%(index)
        book.price = (index)*1.0
        book.title = 'title-%d'%(index)
        book.author = 'author-%s'%(index)
        book.press = 'press-%s'%(index / 10)
        book.description = 'description for book-%d'%(index)
        book.cover = 'cover-%d'%(index)

        book.link = 'http://www.oricinus_price/book-%d-%d'%(index, i%2)
        book.platform = i % 2
        book.instant_price = book.price * 0.8
        book.crawling_time = i

        book_dao.insert(book)

def test_query():
    pair = {"isbn": '00001001'}
    result = book_dao.query_any_matched({'isbn':'00001'})
    for bookpo in result:
        print bookpo.isbn, bookpo.price

if __name__=="__main__":
    test_query()
