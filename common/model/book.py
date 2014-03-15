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
