# -*- coding: utf-8 -*-
__author__ = 'Dazdingo'

import pymongo


class BookPipeline(object):

    @staticmethod
    def process_item(item, spider):
        con = pymongo.Connection('localhost', 27017)
        db = con.testspider
        if item['platform'] == -1:
            return item
        if not item['ISBN']:
            item['platform'] = -1
            return item
        if item['platform'] == 3:       # if item is comments return to detail_pipeline
            return item

        db_data = {"ISBN": "", "name": "", "price": "", "author": "",
                   "press": "", "instant": "", "img": "", "description": ""}
        if item['name']:
            db_data['name'] = item['name'][0]
        if item['price']:
            db_data['price'] = item['price'][0]
        if item['author']:
            db_data['author'] = item['author'][0]
        if item['press']:
            db_data['press'] = item['press'][0]
        if item['instant']:
            db_data['instant'] = item['instant'][0]
        if item['img']:
            db_data['img'] = item['img'][0]
        if item['description']:
            db_data['description'] = item['description'][0]
        db_data['ISBN'] = item['ISBN'][0]

        db.booklist.insert(db_data)
        return item


class DetailPipeline(object):

    @staticmethod
    def process_item(item, spider):
        con = pymongo.Connection('localhost', 27017)
        db = con.testspider
        if item['platform'] != 3:
            return item
        db_data = {"ISBN": "", "author": "", "detail": "", "comment_time": ""}
        if item['ISBN']:
            db_data['isbn'] = item['ISBN']
        if item['author']:
            db_data['author'] = item['author']
        if item['detail']:
            db_data['detail'] = item['detail'][0]
        if item['comment_time']:
            db_data['comment_time'] = item['comment_time'][0]
        db.booklist.insert(db_data)
        return item
