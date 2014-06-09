# -*- coding: utf-8 -*-
__author__ = 'Dazdingo'

import re
from scrapy.spider import Spider
from scrapy.selector import Selector
from crawl.items import DetailItem
from scrapy.http.request import Request


class DoubanSpider(Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = ["http://book.douban.com/tag/"]
    url_head = "http://book.douban.com"

    info_path = '//div[@class="indent subject-info"]/div'
    ISBN_path = re.compile(u'isbn.*</span>.(\d*)<br>')
    author_path = re.compile(u'作者:</span>(.*)<br>')
    comment_time_path = '//span[@class="mn"]/@content'
    detail_path = '//span[@property="v:description"]/text()'

    platform_code = 3  # 豆瓣代码是3

    def catch_item(self, response):  # 抓取书本
        selector = Selector(response)
        item = DetailItem()
        item['url'] = response.url
        info_div = selector.xpath(self.info_path).extract()
        item['ISBN'] = self.ISBN_path.findall(info_div[0])[0].replace(u' ', '')
        item['author'] = self.author_path.findall(info_div[0])[0].replace(u' ', '')
        item['comment_time'] = selector.xpath(self.comment_time_path).extract()
        item['detail'] = selector.xpath(self.detail_path).extract()
        item['platform'] = self.platform_code
        return item

    def parse(self, response):  # 入口
        selector = Selector(response)
        sites = selector.xpath('//table[@class="tagCol"]/tbody/tr/td/a/@href').extract()
        for site in sites:
            request = Request(url=self.replace_url(site),
                              callback=self.view_page)
            yield request

    def view_page(self, response):  # 翻页
        selector = Selector(response)
        sites = selector.xpath('//div[@class="info"]/h2/a/@href').extract()
        for site in sites:
            request = Request(url=site,
                              callback=self.click_comment)
            yield request
        sites = selector.xpath('//span[@class="next"]/a/@href').extract()
        if sites:
            request = Request(url=self.url_head + sites[0],
                              callback=self.view_page)
            yield request

    def click_comment(self, response):  # click_comment
        selector = Selector(response)
        sites = selector.xpath('///div[@class="ctsh"]/div/div/h3/a/@href').extract()
        for site in sites:
            request = Request(url=site,
                              callback=self.catch_item)
            yield request

    def replace_url(self, a_string):
        return a_string.replace(u'.', self.url_head + '/tag')