#!usr/bin/env python
# coding=utf-8
# Author: zhezhiyong@163.com
# Created: 2016-03-02 02:16:53
# Python version：2.7.10

from scrapy_redis.spiders import RedisSpider
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from novelspider.items import NovelspiderItem
from scrapy.http import Request
import re


# class novSpider(RedisSpider):
#     name = "novelspider"
#     redis_key = 'nvospider:start_urls'
#     start_urls = [
#         # 'http://www.lread.net/read/70/'
#         'http://www.daomubiji.com/'
#         # 'http://www.daomubiji.com/qi-xing-lu-wang-01.html'
#     ]
#
#     def parse(self, response):
#         selector = Selector(response)
#         table = selector.xpath('//table')
#         for each in table:
#             bookName = each.xpath('tr/td[@colspan="3"]/center/h2/text()').extract()[0]
#             content = each.xpath('tr/td/a/text()').extract()
#             url = each.xpath('tr/td/a/@href').extract()
#             for i in range(len(url)):
#                 item = NovelspiderItem()  # 为了防止后一个数据覆盖前一个数据，需要在每个循环里都实例化一个NovelspiderItem
#                 item['bookName'] = bookName
#                 item['chapterURL'] = url[i]
#                 # try可以用于检测错误，出现错误以后就会运行except里面的内容。
#                 try:
#                     item['bookTitle'] = content[i].split(' ')[0]
#                     item['chapterNum'] = content[i].split(' ')[1]
#                 except Exception, e:
#                     continue
#
#                 try:
#                     item['chapterName'] = content[i].split(' ')[2]
#                 except Exception, e:
#                     item['chapterName'] = content[i].split(' ')[1][-3:]
#                 yield Request(url[i], callback='parseContent', meta={'item': item})
#
#     def parseContent(self, response):
#         selector = Selector(response)
#         item = response.meta['item']
#         html = selector.xpath('//div[@class="content"]').extract()[0]
#         textField = re.search('<div style="clear:both"></div>(.*?)<div', html, re.S).group(1)
#         text = re.findall('<p>(.*?)</p>', textField, re.S)
#         fulltext = ''
#         for each in text:
#             fulltext += each
#         item['text'] = fulltext
#         yield item

class novelSpider(CrawlSpider):
    name = 'novelspider'
    redis_key = 'novelspider:start_urls'
    url = 'http://www.lread.net'
    start_urls = ['http://www.lread.net/read/70/']
    download_delay = 2

    def parse(self, response):
        selector = Selector(response)
        table = selector.xpath('//dd')
        for node in table:
            if len(node.xpath('a/@href').extract()) != 0:
                print node.xpath('a/@title').extract()[0].encode('utf8')
                print node.xpath('a/@href').extract()
                # table = selector.xpath('//div[@class="box_con"]')[1]
                # print table
                # print table.xpath('dd')
                # for each in table:
                #     print 111, each
                #     print each.xpath('dt')
                # bookName = each.xpath('tr/td[@colspan="3"]/center/h2/text()').extract()[0]
                # content = each.xpath('tr/td/a/text()').extract()
                # url = each.xpath('tr/td/a/@href').extract()
                # for i in range(len(url)):
                #     item = NovelspiderItem()  # 为了防止后一个数据覆盖前一个数据，需要在每个循环里都实例化一个NovelspiderItem
                #     item['bookName'] = bookName
                #     item['chapterURL'] = url[i]
                #     # try可以用于检测错误，出现错误以后就会运行except里面的内容。
                #     try:
                #         item['bookTitle'] = content[i].split(' ')[0]
                #         item['chapterNum'] = content[i].split(' ')[1]
                #     except Exception, e:
                #         continue
                #
                #     try:
                #         item['chapterName'] = content[i].split(' ')[2]
                #     except Exception, e:
                #         item['chapterName'] = content[i].split(' ')[1][-3:]
                #     yield item
