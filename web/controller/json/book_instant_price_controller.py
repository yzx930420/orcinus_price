# -*- coding: utf-8 -*-
__author__ = 'nothi'

import json
from tornado.web import RequestHandler
from json import encoder
encoder.FLOAT_REPR = lambda o: format(o, '.2f')

class BookInstantPriceController(RequestHandler):
    def get(self, isbn):
        a = [ {"name":"当当网","data":[{"date":"2012/12/14", "price":30}, {"date":"2013/12/18", "price":40}]},
              {"name":"京东商城","data":[{"date":"2012/12/14", "price":30}, {"date":"2013/12/18", "price":40}]}
        ]
        self.write(json.dumps(a,ensure_ascii=False))

    def post(self, isbn):
        self.get(isbn)