# -*- coding: utf-8 -*-

__author__ = 'nothi'

from tornado.web import RequestHandler

class BookDetailController(RequestHandler):
    def get(self, isbn):
        print "This is the book "  , isbn

    def post(self, isbn):
        print "This is the book " ,isbn
