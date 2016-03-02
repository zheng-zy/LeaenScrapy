#!usr/bin/env python
# coding=utf-8
# Author: zhezhiyong@163.com
# Created: 2016-03-01 01:10:24
# Python version：2.7.10
"""
# TODO(purpose): 
"""
import scrapy
from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    # 名字唯一
    name = 'dmoz'
    allowed_domains = ['dmoz.org']
    # 爬取数据列表
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/"
    ]

    # 该方法负责处理响应返回数据,如Item和URL。
    def parse(self, response):
        items = []
        for sel in response.xpath('//ul[@class="directory-url"]/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            items.append(item)
        return items
        # for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
        #     url = response.urljoin(href.extract())
        #     yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            print item.title
            yield item
