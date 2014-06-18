# -*- coding: utf-8 -*-
"""这里实现了对MYSQL的简单操作(同步的，阻塞的). """
__author__ = 'yzx930420'


import MySQLdb
from common.dao import settings
from common.model.book import Book
from common.model.book_goods_info import BookGoodsInfo as GoodsPO
from common.model.book_info import BookInfo as  BookPO


class BookDAO():
    def __init__(self):
        self.conn = MySQLdb.connect(host=settings.MYSQL_URL,
                                    user=settings.MYSQL_USER,
                                    passwd=settings.MYSQL_PASSWORD,
                                    db=settings.MYSQL_DATABASE,
                                    charset="utf8" )
        self.cursor = self.conn.cursor()
        self.cursor.execute("set names utf8")
        self.conn.commit();

    def quey_by_isbn(self, isbn):
        """
            通过isbn查找图书，返回图书的信息，结果唯一
            @parms isbn 要查找书的ISBN
            @return BookInfo类型
        """
        attrs = ["isbn", "price", "title", "author", "press","description","cover" ]
        quey_sql = 'select isbn, price, title, author, press, description, cover ' \
                   'from book_info ' \
                   'where isbn = "%s" '%isbn
        self.cursor.execute(quey_sql)
        list = self.cursor.fetchall()
        if not list:
            return None
        bookInfos = list[0]
        result = BookPO()
        i = 0
        for item in bookInfos:
            result[attrs[i]] = item
            i = i + 1
        return result


    def quey_by_isbn_for_goods(self, isbn):
        """
            查找每个平台最新的,相同平台的只有最新的
        """
        attrs = ["isbn","link","platform","instant_price", "crawling_time"]
        quey_sql = 'select isbn, link, platform, instant_price, crawling_time ' \
                   'from book_goods_info ' \
                   'where isbn = %s order by crawling_time desc'%isbn
        self.cursor.execute(quey_sql)
        result_list = []
        bookInfos_list = self.cursor.fetchall()
        all = {}
        for bookInfos in bookInfos_list:
            result = GoodsPO()
            i = 0
            for item in bookInfos:
                result[attrs[i]] = item
                i = i + 1
            all[result.platform] = result
        result_list = all.values()
        return result_list

    def quey_by_isbn_with_time(self, isbn, begin, end):
        attrs = ["isbn","link","platform","instant_price", "crawling_time"]
        quey_sql = 'select isbn, link, platform, instant_price, crawling_time ' \
                   'from book_info ' \
                   'where isbn = %s and crawling_time between %s and %s'%(isbn, begin, end)
        self.cursor.execute(quey_sql)
        result_list = []
        bookInfos_list = self.cursor.fetchall()
        for bookInfos in bookInfos_list:
            result = GoodsPO()
            i = 0
            for item in bookInfos:
                result[attrs[i]] = item
                i = i + 1
            result_list.append(result)
        return result_list

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

        print bookpo.title
        # 判断book_info中是否已经存在
        select_sql = 'select * from book_info where isbn = "%s"' %(bookpo.isbn)
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

    def __parse_book_to_po(self, book):
        #把Book转化为两个PO实体
        #steop1 : book->goods
        goods = GoodsPO()
        goods_attrs = ['isbn', 'instant_price', 'link', 'platform', 'crawling_time']
        for attr in goods_attrs:
            goods[attr] = book[attr]

        #step2 : book->bookpo
        bookpo_attrs = ['description', 'author', 'isbn', 'press', 'title','price','cover']
        bookpo = BookPO()
        for attr in bookpo_attrs:
            bookpo[attr] = book[attr]

        return (goods, bookpo)

    def __parse_po_to_book(self, bookpo, goodspo):
        book = Book()

        #goodspo->book
        goods_attrs = ['isbn', 'instant_price', 'link', 'platform', 'crawling_time']
        for attr in goods_attrs:
            book[attr] = goodspo[attr]

        # bookpo->book
        bookpo_attrs = ['description', 'author', 'isbn', 'press', 'title','price','cover']
        for attr in bookpo_attrs:
            book[attr] = bookpo[attr]

        return book

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
    pair = {"isbn": 'saxsax'}
    result = book_dao.query_any_matched(pair)
    print len(result)
    for bookpo in result:
        print bookpo.isbn, bookpo.title.encode('utf-8')

def test_insert_chinese():
    book = Book()
    book.title = "你好".decode('utf-8')
    book.isbn = 'saxsax'
    book_dao.insert(book)

def test_query_by_isbn():
    a = book_dao.quey_by_isbn("9787509611876")
    print a.isbn
    print a.author
    print a.title

def test_query_by_isbn_for_goods():

    goodses = book_dao.quey_by_isbn_for_goods("9787516301166")
    for a in goodses:
        print a.isbn
        print a.platform
        print a.instant_price

if __name__=="__main__":
    #test_query_by_isbn()
    test_query_by_isbn_for_goods()
