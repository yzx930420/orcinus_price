# -*- coding: utf-8 -*-
__author__ = 'Dazdingo'
from scrapy.spider import Spider
from scrapy.selector import Selector
from crawl.items import BookItem
from scrapy.http.request import Request
import re


class DangdangSpider(Spider):
    name = "dangdang"
    allowed_domains = ["dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.00.00.00.00.00.html"]
    url_head = "http://category.dangdang.com"
    platform_code = 0  # 当当代码是0
    author_path = re.compile(u'作.*者</div>.*\s\s.*green">(.*)</a>')
    press_path = re.compile(u'出.*版.*社</div>.*\s\s.*green">(.*)</a>')
    ISBN_path = re.compile(u'ＩＳＢＮ</div>.*\s\s.*">(.*)</div>')
    img_path = '//img[@id="largePic"]/@wsrc'
    description_path = '//*[@id="content_all"]/p/text()'
    instant_path = '//*[@id="salePriceTag"]/text()'
    price_path = '//*[@id="originalPriceTag"]/text()'
    name_path = '//div[@class="head"]/h1/text()'
    book_box_path = '//div[@class="book_messbox"]'

    def catch_item(self, response):
        selector = Selector(response)
        item = BookItem()
        item['url'] = response.url
        book_box = selector.xpath(self.book_box_path).extract()
        if not book_box:
            item['platform'] = -1
            return item
        item['press'] = self.press_path.findall(book_box[0])
        item['author'] = self.author_path.findall(book_box[0])
        item['ISBN'] = self.ISBN_path.findall(book_box[0])
        item['img'] = selector.xpath(self.img_path).extract()
        item['description'] = selector.xpath(self.description_path).extract()
        item['instant'] = selector.xpath(self.instant_path).extract()
        item['price'] = selector.xpath(self.price_path).extract()
        item['name'] = selector.xpath(self.name_path).extract()
        item['platform'] = self.platform_code
        item['price'][0] = self.replace_rmb(item['price'][0])
        item['instant'][0] = self.replace_rmb(item['instant'][0])
        return item

    def parse(self, response):
        selector = Selector(response)
        sites = selector.xpath('//*[@id="leftCate"]/ul/li/a/@href').extract()
        for site in sites:
            request = Request(url=self.url_head + site,
                              callback=self.open_categories)
            yield request

    def open_categories(self, response):
        selector = Selector(response)
        sites = selector.xpath('//ul/li/div/span/a/@href').extract()
        for site in sites:
            request = Request(url=self.url_head + site,
                              callback=self.view_page)
            yield request

    def view_page(self, response):
        selector = Selector(response)
        sites = selector.xpath('//ul/li/div/p[1]/a/@href').extract()
        for site in sites:
            request = Request(url=site,
                              callback=self.catch_item)
            yield request
        sites = selector.xpath('//*[@id="bd"]/div[3]/div[3]/div[6]/div[2]/div[1]/div[3]/div/a[2]/@href').extract()
        if sites:
            request = Request(url=self.url_head + sites[0],
                              callback=self.view_page)
            yield request

    @staticmethod
    def replace_rmb(a_string):
        return a_string.replace(u'\uffe5', '')