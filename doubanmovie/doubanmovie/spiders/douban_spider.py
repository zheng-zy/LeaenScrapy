#!usr/bin/env python
# coding=utf-8
# Author: zhezhiyong@163.com
# Created: 2016-03-02 02:11:32
# Python version：2.7.10

from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from doubanmovie.items import DoubanmovieItem


class Douban(CrawlSpider):
    name = 'doubanmovie'
    redis_key = 'douban:start_urls'
    start_urls = ['http://movie.douban.com/top250']
    url = 'http://movie.douban.com/top250'

    def parse(self, response):
        item = DoubanmovieItem()
        selector = Selector(response)
        Movies = selector.xpath('//div[@class="info"]')
        for eachMovie in Movies:
            title = eachMovie.xpath('div[@class="hd"]/a/span/text()').extract()
            fullTitle = ''
            for each in title:
                fullTitle+=each
            movieInfo = eachMovie.xpath('div[@class="bd"]/p/text()').extract()
            star = eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            quote = eachMovie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            item['title'] = fullTitle
            item['movieInfo'] = ';'.join(movieInfo)
            item['star'] = star
            item['quote'] = quote
            yield item
        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        if nextLink:
            nextLink = nextLink[0]
            print self.url+nextLink
            yield Request(self.url+nextLink, callback=self.parse)
