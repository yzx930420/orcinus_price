__author__ = 'nothi'

class BookInfo:
    attrs = ["isbn", "price", "title", "author", "press","description","cover" ]

    def __init__(self):
        self.isbn = ''
        self.price = 0.0
        self.title = ''
        self.author = ''
        self.press = ''
        self.description= ''
        self.cover = ''
        self.goods_list = []

    def set_all(self, list):
        self.isbn = list[0]
        self.price = list[1]
        self.title = list[2]
        self.author = list[3]
        self.press = list[4]
        self.desciption = list[5]
        self.cover = list[6]
