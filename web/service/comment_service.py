# -*- coding: utf-8 -*-
__author__ = 'nothi'

from common.dao.comment_dao import comment_dao

COMMENT_SIZE = 4

class CommentService:
    def get_comment(self, isbn):
        return comment_dao.query(isbn, COMMENT_SIZE)
