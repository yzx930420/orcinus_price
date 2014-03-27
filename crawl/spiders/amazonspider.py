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
class amazonSpider(Spider):
    name = "amazon"
    allowed_domains = ["amazon.cn"]
    start_urls = ["http://www.amazon.cn/gp/book/all_category"]
    url_head = "http://www.amazon.cn"

    img_path = '//*[@id="original-main-image"]/@src'
    description_path = '//*[@id="postBodyPS"]/div/text()'
    instant_path = '//*[@id="actualPriceValue"]/b/text()'
    price_path = '//*[@id="listPriceValue"]/text()'
    name_path = '//*[@id="btAsinTitle"]/span/text()'
    press_path = '//td[@class="bucket"]/div/ul/li[1]/text()'
    ISBN_path = '//td[@class="bucket"]/div/ul/li[5]/text()'
    author_path = '//*[@id="handleBuy"]/div[1]/span/a'
    platformcode = 2 #亚马逊代码是1

    def catchitem(self,response):#抓取书本
        selec = Selector(response)
        item = bookItem()
        item['url'] = response.url
        item['press'] = selec.xpath(self.press_path).extract()
        item['author'] = selec.xpath(self.author_path).extract()
        item['ISBN'] = selec.xpath(self.ISBN_path).extract()
        item['img'] = selec.xpath(self.img_path).extract()
        item['description'] = selec.xpath(self.description_path).extract()
        item['instant'] = selec.xpath(self.instant_path).extract()
        item['price'] = selec.xpath(self.price_path).extract()
        item['name'] = selec.xpath(self.name_path).extract()
        item['platform'] = self.platformcode
        item['price'][0] = self.replaceRMB(item['price'][0])
        item['instant'][0] = self.replaceRMB(item['instant'][0])
        item['platform'] = self.platformcode
        return item
    def parse(self, response):#入口
        selec = Selector(response)
        sites = selec.xpath('//a[@class="a-link-nav-icon"]/@href').extract()
        for site in sites:
            print site
            request = Request(url = url_head + site,
                              callback=self.viewpage)
            yield request
    def viewpage(self, response):#翻页
        selec = Selector(response)
        sites = selec.xpath('//h3[@class="newaps"]/a/@href').extract()
        for site in sites:
            request = Request(url = site,
                              callback=self.catchitem)
            yield request
        sites = selec.xpath('//a[@class="pagnNext"]/@href').extract()
        if(len(sites) > 0):
            request = Request(url = url_head + sites[0],
                              callback=self.viewpage)
            yield request

    def replaceRMB(astring):
        return astring.replace(u'\uffe5','')
