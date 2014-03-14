__author__ = 'Dazdingo'

from common.model.book import Book
from common.dao.book_dao import book_dao

class dangdangPipeline(object):

    def process_item(self, item, spider):
        if(len(item['ISBN']) == 0):
            return item
        newbook = Book()
        newbook.title = item["name"][0]
        newbook.price = item["price"][0]
        newbook.isbn = item["ISBN"][0]
        newbook.author = item["author"][0]
        newbook.press = item["press"][0]
        newbook.instant_price = item["instant"][0]
        newbook.link = item["url"]
        newbook.cover = item["img"][0]
        newbook.desc = item["desc"][0]
        newbook.platform = "dangdang"
        #newbook.time = ?
        book_dao.insert(newbook)
