# -*- coding: utf-8 -*-

__author__ = 'nothi'

from os.path import join
from tornado.web import RequestHandler
from web.service.book_service import BookService
from web.settings import *

class BookDetailController(RequestHandler):
    def initialize(self):
        self.service = BookService()

    def get(self, isbn):
        result = self.service.query_by_pair_any({"isbn":isbn})
        result_json = {}
        if len(result) != 0:
            print "okkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
            result_json = result[0].to_dir()
            print type(result[0].to_dir())
            print type(result[0])

        self.write(result_json)
        #from tornado.escape import json_encode
        #print json_encode(result_json)
        # self.write(json_encode(result[0]))
        #self.render(join(template_dir,"bookdetail.html"),list=result)

    def post(self, isbn):
        self.get()
