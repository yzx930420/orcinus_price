# -*- coding: utf-8 -*-

__author__ = 'nothi'
import os
from tornado.web import  RequestHandler
from web.service.book_service import BookService
from web.settings import *

class ResultSetController(RequestHandler):
    def initialize(self):
        self.service = BookService()

    def get(self):
        action = self.get_argument("action")
        keyword = self.get("keyword")
        result = []
        if action == None or action == "any":
           result = self.service.query_by_keyword(keyword)
        else:
            result = self.service.query_by_pair({action:keyword})

        self.render(os.path.join(template_dir, "resultset.html"), list=result)

    def post(self):
        self.get()
