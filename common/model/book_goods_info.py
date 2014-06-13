__author__ = 'nothi'

class BookGoodsInfo:
    attrs = ["isbn","link","platform","instant_price", "crawling_time"]
    def __init__(self):
        self.isbn = ''
        self.link = ''
        self.platform = ''
        self.instant_price = 0.0
        self.crawling_time = ''

    def __getitem__(self, item):
        if "isbn" == item:
            return self.isbn
        elif "link" == item:
            return self.link
        elif "platform" == item:
            return self.platform
        elif "instant_price" == item:
            return self.instant_price
        elif "crawling_time" == item:
            return self.crawling_time

    def __setitem__(self, item, value):
        if "isbn" == item:
            self.isbn = value
        elif "link" == item:
            self.link = value
        elif "platform" == item:
            self.platform = value
        elif "instant_price" == item:
            self.instant_price = value
        elif "crawling_time" == item:
            self.crawling_time = value

    def set_all(self, list):
        self.isbn = list[0]
        self.link = list[1]
        self.platform = list[2]
        self.instant_price = list[3]
        self.crawling_time = list[4]

    def to_dir(self):
        result = {}
        result['isbn'] = self.isbn
        result['link'] = self.link
        result['platform'] = self.platform
        result['instant_price'] = str(self.instant_price)
        result['crawling_time'] = self.crawling_time
        return result
