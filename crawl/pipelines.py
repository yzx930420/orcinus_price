# -*- coding: utf-8 -*-
__author__ = 'Dazdingo'

from scrapy.exceptions import DropItem
import pymongo


class BookPipeline(object):
    con = pymongo.Connection('localhost', 27017)
    db = con.testspider

    def process_item(self, item, spider):
        if not item['ISBN']:            # if item  do not have isbn then drop it
            raise DropItem('Duplicate item found: %s' % item)
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

        print "ok  to  insert ======================="
        try:
            self.db.booklist.insert(db_data)
        except:
            print "=============================="

        return item


class DetailPipeline(object):
    con = pymongo.Connection('localhost', 27017)
    db = con.testspider
    
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):

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