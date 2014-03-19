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
class dangdangSpider(Spider):
    name = "dangdang"
    allowed_domains = ["dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.00.00.00.00.00.html"]
    url_head = "http://category.dangdang.com"
    def catchitem(self,response):
        selec = Selector(response)
        item = bookItem()
        item['url'] = response.url
        tempstr = selec.xpath('//div[@class="book_messbox"]/div[1]/div[1]/text()').extract()
        path = 1
        divauthor = [u'\u4f5c\xa0\xa0\xa0\xa0\xa0\u8005'] #用来识别不同页面排版中 作者在第几个div
        if(tempstr == divauthor):
            path = 1
        else:
            path = 2
        item['img'] = selec.xpath('//img[@id="largePic"]/@wsrc').extract()
        item['description'] = selec.xpath('//*[@id="content_all"]/p/text()').extract()
        item['instant'] = selec.xpath('//*[@id="originalPriceTag"]/text()').extract()
        item['instant'][0] = item['instant'][0].replace(u'\uffe5','')        #处理价格前面的人民币符号
        item['press'] = selec.xpath('//div[@class="book_messbox"]/div[' + str(path + 1) + ']/div[2]/a/text()').extract()
        item['price'] = selec.xpath('//*[@id="salePriceTag"]/text()').extract()
        item['price'][0] = item['price'][0].replace(u'\uffe5','')           #处理价格前面的人民币符号
        item['author'] = selec.xpath('//div[@class="book_messbox"]/div[' + str(path) + ']/div[2]/a/text()').extract()
        item['ISBN'] = selec.xpath('//div[@class="book_messbox"]/div[' + str(path + 3) + ']/div[2]/text()').extract()
        item['name'] = selec.xpath('//div[@class="head"]/h1/text()').extract()
        item['platform'] = 0 #当当代码是0
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