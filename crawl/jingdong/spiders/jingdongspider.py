__author__ = 'Dazdingo'
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.spiders import Rule
from crawl.items import jingdongItem
from scrapy.http.request import Request
from scrapy import log
import string
class jingdongSpider(Spider):
    name = "jingdong"
    allowed_domains = ["jd.com"]
    start_urls = ["http://www.jd.com/book/booksort.aspx"]
    def catchitem(self,response):#TODO
        selec = Selector(response)
        item = jingdongItem()
        item['url'] = response.url
        item['img'] = selec.xpath('//*[@id="spec-n1"]/img/@src').extract()
        #item['desc'] = selec.xpath('//*[@id="content_all"]/p/text()').extract()   bug
        item['instant'] = selec.xpath('//*[@id="summary-market"]/div/del/text()').extract()
        item['press'] = selec.xpath('//*[@id="summary-ph"]/div/a/text()').extract()
        item['price'] = selec.xpath('//*[@id="summary-price"]/div/strong/text()').extract()
        item['author'] = selec.xpath('//*[@id="summary-author"]/div/a/text()').extract()
        item['ISBN'] = selec.xpath('//*[@id="summary-isbn"]/div/text()').extract()
        item['name'] = selec.xpath('//*[@id="name"]/h1/text()').extract()
        tempstr = "".join(item['name'])
        print tempstr
        return item
    def parse(self, response):
        selec = Selector(response)
        sites = selec.xpath('//*[@id="booksort"]/div[@class="mc"]/dl/dd/em/a/@herf').extract()
        for site in sites:
            request = Request(url = self.url_head + site,
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
            request = Request(url = self.url_head + sites[0],
                              callback=self.viewpage)
            yield request