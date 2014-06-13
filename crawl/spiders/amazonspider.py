# -*- coding: utf-8 -*-
__author__ = 'Dazdingo'
from scrapy.spider import Spider
from scrapy.selector import Selector
from crawl.items import BookItem
from scrapy.http.request import Request
import re


class AmazonSpider(Spider):
    name = "amazon"
    allowed_domains = ["amazon.cn"]
    start_urls = ["http://www.amazon.cn/gp/book/all_category"]
    url_head = "http://www.amazon.cn"

    info_path = '//td[@class="bucket"]/div[@class="content"]/ul'
    img_path = '//*[@id="original-main-image"]/@src'
    description_path = '//*[@id="postBodyPS"]/div/text()'
    instant_path = '//*[@id="actualPriceValue"]/b/text()'
    price_path = '//*[@id="listPriceValue"]/text()'
    name_path = '//*[@id="btAsinTitle"]/span/text()'
    press_path = re.compile(u'出版社.*</b>.(.*)</li>')
    ISBN_path = re.compile(u'ISBN.*</b>.(\d*).')
    author_path = '//*[@id="handleBuy"]/div[1]/span/a/text()'
    platform_code = 2  # 亚马逊代码是2

    def catch_item(self, response):  # 抓取书本
        selector = Selector(response)
        item = BookItem()
        item['url'] = response.url
        info_div = selector.xpath(self.info_path).extract()
        item['press'] = self.press_path.findall(info_div[0])
        item['author'] = selector.xpath(self.author_path).extract()
        item['ISBN'] = self.ISBN_path.findall(info_div[0])
        item['img'] = selector.xpath(self.img_path).extract()
        item['description'] = selector.xpath(self.description_path).extract()
        item['instant'] = selector.xpath(self.instant_path).extract()
        item['price'] = selector.xpath(self.price_path).extract()
        item['name'] = selector.xpath(self.name_path).extract()
        item['platform'] = self.platform_code
        item['price'][0] = self.replace_rmb(item['price'][0])
        item['instant'][0] = self.replace_rmb(item['instant'][0])
        item['platform'] = self.platform_code
        return item

    def parse(self, response):  # 入口
        selector = Selector(response)
        sites = selector.xpath('//a[@class="a-link-nav-icon"]/@href').extract()
        for site in sites:
            request = Request(url=self.url_head + site,
                              callback=self.view_page)
            if request.url.startswith("http://www.amazon.cn/b?ie=UTF8&node=658810051"):
                yield request

    def view_page(self, response):  # 翻页
        selector = Selector(response)
        sites = selector.xpath('//h3[@class="newaps"]/a/@href').extract()
        for site in sites:
            request = Request(url=site,
                              callback=self.catch_item)
            yield request
        sites = selector.xpath('//a[@class="pagnNext"]/@href').extract()
        if sites:
            request = Request(url=self.url_head + sites[0],
                              callback=self.view_page)
            yield request

    @staticmethod 
    def replace_rmb(a_string):
        return a_string.replace(u'\uffe5', '')
