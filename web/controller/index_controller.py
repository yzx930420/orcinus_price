# -*- coding: utf-8 -*-
__author__ = 'nothi'

from tornado.web import RequestHandler
from web.settings import *

class IndexController(RequestHandler):
    def get(self):
       file = os.path.join(settings['template_path'], "index.html")
       self.render(file)

    def post(self):
        self.get()



