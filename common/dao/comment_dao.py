# -*- coding: utf-8 -*-
__author__ = 'nothi'

import MySQLdb
import common.dao.settings
from common.model.comment import Comment

class CommentDAO:
    def __init__(self):
        self.conn = MySQLdb.connect(host=common.dao.settings.MYSQL_URL,
                                    user=common.dao.settings.MYSQL_USER,
                                    passwd=common.dao.settings.MYSQL_PASSWORD,
                                    db=common.dao.settings.MYSQL_DATABASE,
                                    charset="utf8" )
        self.cursor = self.conn.cursor()
        self.cursor.execute("set names utf8")
        self.conn.commit();

    def insert(self, comment):
        print comment
        statement = 'insert into comment(isbn, author, comment_time, detail,link) ' \
                    'values(%s, %s, %s, %s)'
        self.cursor.execute(statement, [comment.isbn,
                                        comment.author,
                                        comment.comment_time,
                                        comment.detail,
                                        comment.link
        ])

    def query(self, isbn, max_size):
        pass

comment_dao = CommentDAO()
