# -*- coding: utf-8 -*-
__author__ = 'nothi'

from common.dao.comment_dao import comment_dao

COMMENT_SIZE = 4

class CommentService:
    def get_comment(self, isbn):
        if type(isbn) == type(b"unicode"):
            isbn = isbn.encode('utf-8')
        return comment_dao.query(isbn, COMMENT_SIZE)
