# -*- coding: utf-8 -*-
__author__ = 'nothi'

class Comment:
    def __init__(self):
        self.isbn = ""
        self.author = ""
        self.comment_time = ""
        self.detail = ""
        self.link = ""

    def __str__(self):
        return "isbn "+self.isbn + "author "+self.author+"comment_time"+\
               self.comment_time+"detail "+self.detail + " link " + self.link
