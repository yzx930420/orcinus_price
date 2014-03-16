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
        result = self.service.query_by_pair({"isbn":isbn})
        self.render(join(template_dir,"bookdetail.html"),list=result)

    def post(self, isbn):
        self.get()
