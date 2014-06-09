# -*- coding: utf-8 -*-
__author__ = 'Dazdingo'

from scrapy.exceptions import DropItem


class BookPipeline(object):
    def process_item(self, item, spider):
        if not item['ISBN']:            # if item  do not have isbn then drop it
            raise DropItem('Duplicate item found: %s' % item)
        if item['platform'] == 3:       # if item is comments return to detail_pipeline
            print "over to here"
            return item




class DetailPipeline(object):
    """
    def __init__(self):
        self.ids_seen = set()
    """

    def process_item(self, item, spider):

        if item['platform'] != 3:
            return item

        print "==========ok to insert"

