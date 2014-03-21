# -*- coding: utf-8 -*-
__author__ = 'Dazdingo'
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.spiders import Rule
from crawl.items import bookItem
from scrapy.http.request import Request
from scrapy import log
import string
import re




class dangdangSpider(Spider):
    name = "dangdang"
    allowed_domains = ["dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.00.00.00.00.00.html"]
    url_head = "http://category.dangdang.com"
    platformcode = 0 #当当代码是0
    keymap = [(re.compile(u'作(.*)者'),'author','./a/text()'),
          (re.compile(u'出(.*)版(.*)社'),'press','./a/text()'),
          (re.compile(u'ISBN'),'ISBN','./text()')]
    img_path = '//img[@id="largePic"]/@wsrc'
    description_path = '//*[@id="content_all"]/p/text()'
    instant_path = '//*[@id="salePriceTag"]/text()'
    price_path = '//*[@id="originalPriceTag"]/text()'
    name_path = '//div[@class="head"]/h1/text()'
    bookbox_path = '//div[@class="book_messbox"]'

    def catchitem(self,response):
        selec = Selector(response)
        item = bookItem()
        item['url'] = response.url
        bookbox = selec.xpath(self.bookbox_path)
        for message in bookbox.xpath('./div[@class="clearfix m_t6"]'):
            left = message.xpath('./div[@class="show_info_left"]/text()').extract()[0]
            right = message.xpath('./div[@class="show_info_right"]')
            for pat,name,value_path in self.keymap:
                if pat.match(left):
                    item[name] = right.xpath(value_path).extract()
                    print "======================",name,right

        item['img'] = selec.xpath(self.img_path).extract()
        item['description'] = selec.xpath(self.description_path).extract()
        item['instant'] = selec.xpath(self.instant_path).extract()
        item['price'] = selec.xpath(self.price_path).extract()
        item['name'] = selec.xpath(self.name_path).extract()
        item['platform'] = self.platformcode
        return item

    def parse(self, response):
        selec = Selector(response)
        sites = selec.xpath('//*[@id="leftCate"]/ul/li/a/@href').extract()
        for site in sites:
            request = Request(url = self.url_head + site,
                              callback=self.opencategories)
            yield request
    def opencategories(self, response):
        selec = Selector(response)
        sites = selec.xpath('//ul/li/div/span/a/@href').extract()
        for site in sites:
            request = Request(url = self.url_head + site,
                              callback=self.viewpage)
            yield request
    def viewpage(self, response):
        selec = Selector(response)
        sites = selec.xpath('//ul/li/div/p[1]/a/@href').extract()
        for site in sites:
            request = Request(url = site,
                              callback=self.catchitem)
            yield request
        sites = selec.xpath('//*[@id="bd"]/div[3]/div[3]/div[6]/div[2]/div[1]/div[3]/div/a[2]/@href').extract()
        if(len(sites) > 0):
            request = Request(url = self.url_head + sites[0],
                              callback=self.viewpage)
            yield request

    def replaceRMB(astring):
        return astring.replace(u'\uffe5','')