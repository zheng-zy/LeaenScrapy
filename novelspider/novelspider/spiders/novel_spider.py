#!usr/bin/env python
# coding=utf-8
# Author: zhezhiyong@163.com
# Created: 2016-03-02 02:16:53
# Python version：2.7.10

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from novelspider.items import NovelspiderItem


class novelSpider(CrawlSpider):
    name = 'novelspider'
    redis_key = 'novelspider:start_urls'
    start_urls = ['http://www.daomubiji.com/']

    def parse(self, response):
        selector = Selector(response)
        table = selector.xpath('//table')
        for each in table:
            bookName = each.xpath('tr/td[@colspan="3"]/center/h2/text()').extract()[0]
            content = each.xpath('tr/td/a/text()').extract()
            url = each.xpath('tr/td/a/@href').extract()
            for i in range(len(url)):
                item = NovelspiderItem()  # 为了防止后一个数据覆盖前一个数据，需要在每个循环里都实例化一个NovelspiderItem
                item['bookName'] = bookName
                item['chapterURL'] = url[i]
                # try可以用于检测错误，出现错误以后就会运行except里面的内容。
                try:
                    item['bookTitle'] = content[i].split(' ')[0]
                    item['chapterNum'] = content[i].split(' ')[1]
                except Exception, e:
                    continue

                try:
                    item['chapterName'] = content[i].split(' ')[2]
                except Exception, e:
                    item['chapterName'] = content[i].split(' ')[1][-3:]
                yield item
