__author__ = 'nothi'

class BookGoodsInfo:
    attrs = ["isbn","link","platform","instant_price", "crawling_time"]
    def __init__(self):
        self.isbn = ''
        self.link = ''
        self.platform = ''
        self.instant_price = 0.0
        self.crawling_time = ''

    def set_all(self, list):
        self.isbn = list[0]
        self.link = list[1]
        self.platform = list[2]
        self.instant_price = list[3]
        self.crawling_time = list[4]
