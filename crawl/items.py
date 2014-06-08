__author__ = 'Dazdingo'

from scrapy.item import Item, Field


class BookItem(Item):
    price = Field()
    ISBN = Field()
    name = Field()
    author = Field()
    press = Field()
    url = Field()
    instant = Field()
    img = Field()
    description = Field()
    platform = Field()


class DetailItem(Item):
    ISBN = Field()
    url = Field()
    comment_time = Field()
    author = Field()
    detail = Field()
    platform = Field()