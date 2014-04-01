__author__ = 'nothi'


class Book(object):
    attrs = ["isbn", "price", "title","author", "press", "description", "cover", "link", "platform", "instant_price","crawling_time"]

    def __init__(self):
        self.isbn = ''
        self.price = 0.0
        self.title = ''
        self.author = ''
        self.press = ''
        self.description= ''
        self.cover = ''
        self.link = ''
        self.platform = ''
        self.instant_price = ''
        self.crawling_time = 0

    def set_all(self, list):
        self.isbn = list[0]
        self.price = list[1]
        self.title = list[2]
        self.author = list[3]
        self.press = list[4]
        self.description= list[5]
        self.cover = list[6]
        self.link = list[7]
        self.platform = list[8]
        self.instant_price = list[9]
        self.crawling_time = list[10]

    def __str__(self):
        return "isbn=%s" %(self.isbn)
