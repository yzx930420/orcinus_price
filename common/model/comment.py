# -*- coding: utf-8 -*-
__author__ = 'nothi'

class Comment:
    attrs = ["isbn", "author", "comment_time", "detail", "link"]
    def __init__(self):
        self.isbn = ""
        self.author = ""
        self.comment_time = ""
        self.detail = ""
        self.link = ""

    def to_dict(self):
        result = {
           #'isbn' :self.isbn,
           'author':self.author,
           #'comment_time':self.comment_time,
           #'detail':self.detail,
           #'link':self.link
           "platform":u"豆瓣",
           "content":self.detail
        }
        return result

    def __getitem__(self, key):
        if "isbn" == key:
            return self.isbn
        elif "author" == key:
            return self.author
        elif "comment_time" == key:
            return self.comment_time
        elif "detail" == key:
            return self.detail
        elif "link" == key:
            return self.link

    def __setitem__(self, key, value):
        if "isbn" == key:
            self.isbn = value
        elif "author" == key:
            self.author = value
        elif "comment_time" == key:
            self.comment_time = value
        elif "detail" == key:
            self.detail = value
        elif "link" == key:
            self.link = value

