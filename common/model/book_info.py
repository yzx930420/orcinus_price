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

    def to_dir(self):
        result = {}
        result['isbn'] = self.isbn
        result['price'] = str(self.price)
        result['title'] = self.title
        result['author']  = self.author
        result['press'] = self.press
        result['description'] = self.description
        result['cover'] = self.cover
        #for item in self.goods_list:
        #    result['goods_list'].append(item.to_dir)
        print result
        return result

    def set_all(self, list):
        self.isbn = list[0]
        self.price = list[1]
        self.title = list[2]
        self.author = list[3]
        self.press = list[4]
        self.desciption = list[5]
        self.cover = list[6]
