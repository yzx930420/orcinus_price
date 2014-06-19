# -*- coding: utf-8 -*-
__author__ = 'nothi'

import json
from web.service.book_service import BookService
from tornado.web import RequestHandler
from json import encoder
encoder.FLOAT_REPR = lambda o: format(o, '.2f')

class BookInstantPriceController(RequestHandler):
    def initialize(self):
        self.service = BookService()

    @staticmethod
    def get_platfrom_name(platform):
        platfom_name = {
            0:"当当网",
            1:"京东商城",
            2:"亚马逊"
        }
        return platfom_name[platform]

    def get(self, isbn):
        """
        a = [ {"name":"当当网","data":[{"date":"2012/12/14", "price":30}, {"date":"2013/12/18", "price":40}]},
              {"name":"京东商城","data":[{"date":"2012/12/14", "price":30}, {"date":"2013/12/18", "price":40}]}
        ]
        """
        bookinfo = self.service.quey_by_isbn(isbn)
        a = []
        for goods in bookinfo.goods_list:
            item = {
                "name":self.get_platfrom_name(goods.platform),
                "data":[
                    {"data":"2014/06/1", "price":float(goods.instant_price)},
                    {"data":"2014/06/12", "price":float(goods.instant_price)},
                ]
            }
            a.append(item)
        self.write(json.dumps(a,ensure_ascii=False))

    def post(self, isbn):
        self.get(isbn)