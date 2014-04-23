# -*- coding: utf-8 -*-
__author__ = 'Dazdingo'

from scrapy.exceptions import DropItem
from crawl.items import BookItem
from crawl.items import DetailItem
from common.dao.book_dao import book_dao
from common.model.book import Book


class BookPipeline(object):
    def process_item(self, item, spider):
        if not item['ISBN']:            # if item  do not have isbn then drop it
            raise DropItem('Duplicate item found: %s' % item)
        if item['platform'] == 3:       # if item is comments return to detail_pipeline
            return item

        new_book = Book()
        if item["name"]:
            new_book.title = item["name"][0]
        if item["price"]:
            new_book.price = item["price"][0]
        if item["author"]:
            new_book.author = item["author"][0]
        if item["press"]:
            new_book.press = item["press"][0]
        if item["instant"]:
            new_book.instant_price = item["instant"][0]
        if item["img"]:
            new_book.cover = item["img"][0]
        if item["description"]:
            new_book.description = item["description"][0]
        new_book.isbn = item["ISBN"][0]
        new_book.link = item["url"]
        new_book.platform = item['platform']
        #new_book.time = ?
        new_book.platform = item['platform']
        book_dao.insert(new_book)


class DetailPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        """
        if item['platform'] != 3:
            return item
        if item['ISBN'] in self.ids_seen:
            raise DropItem('Duplicate item found: %s' % item['ISBN'])
        else:
            db_data = {"ISBN": "", "evaluation": "",
                       "evaluation_people": "", "hot_comments": ""}
            self.ids_seen.add(item['ISBN'])
            db_data['ISBN'] = item['ISBN']
            if item['evaluation']:
                db_data['evaluation'] = item['evaluation'][0]
            if item['hot_comments']:
                db_data['hot_comments'] = item['hot_comments']
            if item['evaluation_people']:
                db_data['evaluation_people'] = item['evaluation_people'][0]

            print "ok  to  insert ======================="
            self.db.comments.insert(db_data)

        return item
        """
        pass
