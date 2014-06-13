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

    def __getitem__(self, item):
        if "isbn" == item:
            return self.isbn
        elif "price" == item:
            return self.price
        elif "title" == item:
            return self.title
        elif "author" == item:
            return self.author
        elif "press" == item:
            return self.press
        elif "description" == item:
            return self.description
        elif "cover" == item:
            return self.cover
        elif "link" == item:
            return self.link
        elif "platform" == item:
            return self.platform
        elif "instant_price'" == item:
            return self.instant_price
        elif "crawling_time'" == item:
            return self.crawling_time


    def __setitem__(self, item, value):
        if "isbn" == item:
            self.isbn = value
        elif "price" == item:
            self.price = value
        elif "title" == item:
            self.title = value
        elif "author" == item:
            self.author = value
        elif "press" == item:
            self.press = value
        elif "description" == item:
            self.description = value
        elif "cover" == item:
            self.cover = value
        elif "link" == item:
            self.link = value
        elif "platform" == item:
            self.platform =value
        elif "instant_price'" == item:
            self.instant_price = value
        elif "crawling_time'" == item:
            self.crawling_time = value

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
