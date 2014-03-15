__author__ = 'Dazdingo'

from scrapy.item import Item, Field

class jingdongItem(Item):
    price = Field()
    ISBN = Field()
    name = Field()
    author = Field()
    press = Field()
    url = Field()
    instant = Field()
    img = Field()
    desc = Field()
