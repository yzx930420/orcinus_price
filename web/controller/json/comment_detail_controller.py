# -*- coding: utf-8 -*-
__author__ = 'nothi'

import json
from tornado.web import RequestHandler
from web.service.comment_service import CommentService

class CommentDetailController(RequestHandler):
    def initialize(self):
        self.service = CommentService()

    def get(self, isbn):
        comments = self.service.get_comment(isbn)
        if not comments:
            self.write("")
        else:
            results = []
            for comment in comments:
                results.append(comment.to_dict())
                self.write(json.dumps(results,ensure_ascii=False) )

    def post(self, isbn):
        return self.get(isbn)
