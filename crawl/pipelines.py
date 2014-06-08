# -*- coding: utf-8 -*-
__author__ = 'Dazdingo'

from scrapy.exceptions import DropItem
from crawl.items import BookItem
from crawl.items import DetailItem
from common.dao.book_dao import book_dao
from common.model.book import Book
from common.model.comment import Comment


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
    """
    def __init__(self):
        self.ids_seen = set()
    """

    def process_item(self, item, spider):

        if item['platform'] != 3:
            return item
        #new_comment =
        """
        if item['ISBN'] in self.ids_seen:
            raise DropItem('Duplicate item found: %s' % item['ISBN'])
        else:
        """
        new_comment = Comment()

        if item['author']:
            new_comment['author'] = item['author'][0]
        if item['hot_comments']:
            new_comment['detail'] = item['detail'][0]
        if item['comment_time']:
            new_comment['comment_time'] = item['comment_time'][0]

        print "ok  to  insert ======================="
        # TODO

        return item

    pass
