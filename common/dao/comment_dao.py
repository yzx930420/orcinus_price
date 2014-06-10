# -*- coding: utf-8 -*-
__author__ = 'nothi'

import MySQLdb
import common.dao.settings
from common.model.comment import Comment

import sys
reload(sys)
sys.setdefaultencoding('utf8')

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
        #print comment.isbn
        statement = 'insert into comment(isbn, author, comment_time, detail,link) ' \
                    'values(%s, %s, %s, %s, %s)'
        self.cursor.execute(statement, [comment.isbn,
                                        comment.author,
                                        comment.comment_time,
                                        comment.detail,
                                        comment.link
        ])
        self.conn.commit()

    def query(self, isbn, max_size):
        sql = 'select isbn, author, comment_time, detail, link ' \
              'from comment ' \
              'where isbn="%s" limit %d; ' %(isbn,max_size)

        keys = ("isbn", "author", "comment_time", "detail", "link")
        print sql
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        comments = []
        for result in results:
            comment = Comment()
            i = 0
            for key in keys:
                comment[key] = result[i]
                i = i + 1
            comments.append(comment)
        return comments;

comment_dao = CommentDAO()

def test_quey():
    comments = comment_dao.query("7540202505", 10)

if __name__ == "__main__":
    test_quey()
