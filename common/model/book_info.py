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

    def __setitem__(self, key, value):
        if "isbn" == key:
           self.isbn = value
        elif "price" == key:
            self.price = value
        elif "title" == key:
            self.title = value
        elif "author" == key:
            self.author = value
        elif "press" == key:
            self.press = value
        elif "description" == key:
            self.description = value
        elif "cover" == key:
            self.cover = value
        elif "goods_list" == key:
            self.goods_list = value

    def __getitem__(self, item):
        if "isbn" == item:
            return self.isbn
        elif "price" == item:
            return self.price
        elif "title" == item:
            return self.title
        elif "author" == item:
            return  self.author
        elif "press" == item:
            return self.press
        elif "description" == item:
            return self.desciption
        elif "cover" == item:
            return self.cover
        elif "goods_list" == item:
            return self.goods_list

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
