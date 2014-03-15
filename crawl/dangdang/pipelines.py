__author__ = 'Dazdingo'

from common.model.book import Book
from common.dao.book_dao import book_dao
#import pymongo

class Pipeline(object):
    con = pymongo.Connection("localhost", 27017)
    db = con.bestbuyer
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
        #newbook.desc = item["desc"][0]
        newbook.platform = "dangdang"
        #newbook.time = ?
        book_dao.insert(newbook)
    #def process_item(self, item, spider):
    #    if(len(item['ISBN']) == 0):
    #    	return item
    #    dbdata = {"name":"","price":"","ISBN":"","author":"","press":"","img":"","desc":""}
    #    dbdata["name"] = item["name"][0]
    #    dbdata["price"] = item["price"][0]
    #    dbdata["ISBN"] = item["ISBN"][0]
    #    dbdata["author"] = item["author"][0]
    #    dbdata["press"] = item["press"][0]
    #    dbdata["img"] = item["img"][0]
    #    dbdata["desc"] = item["desc"]
    #    self.db.bookInfo.insert(dbdata)
    #    return item