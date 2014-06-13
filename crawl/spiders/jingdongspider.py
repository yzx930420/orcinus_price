# -*- coding: utf-8 -*-
__author__ = 'Dazdingo'
from scrapy.spider import Spider
from scrapy.selector import Selector
from crawl.items import BookItem
from scrapy.http.request import Request


class JingdongSpider(Spider):
    name = "jingdong"
    allowed_domains = ["jd.com"]
    start_urls = ["http://www.jd.com/book/booksort.aspx"]

    @staticmethod
    def catch_item(response):  # 抓取书本
        selector = Selector(response)
        item = BookItem()
        item['url'] = response.url
        item['img'] = selector.xpath('//*[@id="spec-n1"]/img/@src').extract()
        item['description'] = selector.xpath('//div[@class="con"]/text()').extract()
        item['instant'] = selector.xpath('//*[@id="summary-price"]/div[2]/strong/text()').extract()
        if item['instant']:
            item['instant'][0] = item['instant'][0].replace(u'\uffe5', '')        # 处理价格前面的人民币符号
        item['press'] = selector.xpath('//*[@id="summary-ph"]/div[2]/a/text()').extract()
        item['price'] = selector.xpath('//*[@id="summary-market"]/div[2]/del/text()').extract()
        if item['price']:
            item['price'][0] = item['price'][0].replace(u'\uffe5', '')            # 处理价格前面的人民币符号
        item['author'] = selector.xpath('//*[@id="summary-author"]/div[2]/a/text()').extract()
        item['ISBN'] = selector.xpath('//*[@id="summary-isbn"]/div[2]/text()').extract()
        item['name'] = selector.xpath('//*[@id="name"]/h1/text()').extract()
        item['platform'] = 1  # 京东代码是1
        return item

    def parse(self, response):  # 入口
        selector = Selector(response)
        sites = selector.xpath('//*[@id="booksort"]/div[2]/dl/dd/em/a/@href').extract()
        for site in sites:
            request = Request(url=site,
                              callback=self.view_page)
            if request.url.startswith("http://list.jd.com/1713-3287-3797.html"):
                yield request

    def view_page(self, response):  # 翻页
        selector = Selector(response)
        sites = selector.xpath('//*[@id="plist"]/div/dl/dt/a/@href').extract()
        for site in sites:
            request = Request(url=site,
                              callback=self.catch_item)
            yield request
        sites = selector.xpath('//div[@class="pagin pagin-m"]/a/@href').extract()
        if sites:
            request = Request(url=sites[0],
                              callback=self.view_page)
            yield request
