# -*- coding: utf-8 -*-
__author__ = 'Dazdingo'




class BookPipeline(object):
    def process_item(self, item, spider):

        if item['platform'] == -1:
            return item
        if not item['ISBN']:
            item['platform'] = -1
            return item
        if item['platform'] == 3:       # if item is comments return to detail_pipeline
            return item

        print "=========================================="
        print "startstartstartstartstartstartstartstart"
        print item["name"][0]
        print item["price"][0]
        if item['author']:
            print item["author"][0].replace(u'\u2022', '')
        print item["press"][0]
        print item["instant"][0]
        print item["img"][0]
        #print item["description"][0]
        print item['ISBN']
        print "endendendendendendendendendendendendendend"
        print "=========================================="

        return item



class DetailPipeline(object):
    """
    def __init__(self):
        self.ids_seen = set()
    """

    def process_item(self, item, spider):

        if item['platform'] != 3:
            return item
        print "=========================================="
        print "startstartstartstartstartstartstartstart"

        print item['ISBN']
        print item['author']
        print item['detail'][0]
        print item['comment_time'][0]
        print "endendendendendendendendendendendendendend"
        print "=========================================="

