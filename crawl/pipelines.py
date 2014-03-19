# -*- coding: utf-8 -*-
__author__ = 'Dazdingo'

from common.dao.book_dao import book_dao
from common.model.book import Book

class Pipeline(object):
    def process_item(self, item, spider):
        if(len(item['ISBN']) == 0):
            return item
        newbook = Book()
        newbook.title = item["name"][0]

        newbook.price = item["instant"][0];

        newbook.isbn = item["ISBN"][0]
        newbook.author = item["author"][0]
        newbook.press = item["press"][0]

        newbook.instant_price= item["price"][0];

        newbook.link = item["url"]
        newbook.cover = item["img"][0]
        if len(item["description"]) != 0:
            newbook.description = item["description"][0]
        #newbook.time = ?
        newbook.platform = item['platform']
        print '0----------------------------------',newbook.instant_price
        book_dao.insert(newbook)
