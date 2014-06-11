# -*- coding: utf-8 -*-
__author__ = 'Dazdingo'

from scrapy.exceptions import DropItem
from common.dao.book_dao import book_dao
from common.model.book import Book
from common.model.comment import Comment
from common.dao.comment_dao import comment_dao


class BookPipeline(object):

    @staticmethod
    def process_item(self, item, spider):
        if item['platform'] == -1:      # not a book, drop it
            return item
        if not item['ISBN']:            # not a book, drop it
            item['platform'] = -1
            return item
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

    @staticmethod
    def process_item(self, item, spider):

        if item['platform'] != 3:
            return item

        if not item['ISBN']:
            raise DropItem('item no isbn')

        new_comment = Comment()

        if item['ISBN']:
            new_comment['isbn'] = item['ISBN']
        if item['author']:
            new_comment['author'] = item['author']
        if item['detail']:
            new_comment['detail'] = item['detail'][0]
        if item['comment_time']:
            new_comment['comment_time'] = item['comment_time'][0]

        comment_dao.insert(new_comment)

        return item

    pass
