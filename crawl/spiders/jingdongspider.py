__author__ = 'Dazdingo'
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.spiders import Rule
from crawl.items import bookItem
from scrapy.http.request import Request
from scrapy import log
import string
class jingdongSpider(Spider):
    name = "jingdong"
    allowed_domains = ["jd.com"]
    start_urls = ["http://www.jd.com/book/booksort.aspx"]
    def catchitem(self,response):#TODO
        selec = Selector(response)
        item = bookItem()
        item['url'] = response.url
        item['img'] = selec.xpath('//*[@id="spec-n1"]/img/@src').extract()
        item['description'] = selec.xpath('//*[@id="product-detail-1"]/div[2]/div[2]/div[1]/text()').extract()
        item['instant'] = selec.xpath('//*[@id="summary-market"]/div[2]/del/text()').extract()
        item['press'] = selec.xpath('//*[@id="summary-ph"]/div[2]/a/text()').extract()
        item['price'] = selec.xpath('//*[@id="summary-price"]/div[2]/strong/text()').extract()
        item['author'] = selec.xpath('//*[@id="summary-author"]/div[2]/a/text()').extract()
        item['ISBN'] = selec.xpath('//*[@id="summary-isbn"]/div[2]/text()').extract()
        item['name'] = selec.xpath('//*[@id="name"]/h1/text()').extract()
        tempstr = "".join(item['name'])
        print tempstr
        return item
    def parse(self, response):
        selec = Selector(response)
        sites = selec.xpath('//*[@id="booksort"]/div[2]/dl/dd/em/a/@href').extract()
        for site in sites:
            print site
            request = Request(url = site,
                              callback=self.viewpage)
            yield request
    def viewpage(self, response):
        selec = Selector(response)
        sites = selec.xpath('//*[@id="plist"]/div/dl/dt/a/@href').extract()
        for site in sites:
            request = Request(url = site,
                              callback=self.catchitem)
            yield request
        sites = selec.xpath('//div[@class="pagin pagin-m"]/a/@href').extract()
        if(len(sites) > 0):
            request = Request(url = sites[0],
                              callback=self.viewpage)
            yield request