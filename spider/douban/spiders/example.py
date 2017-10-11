# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


# 第一个example.获取豆瓣新电影排行页面数据
class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["movie.douban.com"]
    start_urls = ['https://movie.douban.com/chart']

    def parse(self, response):
        # print response.body
        for i in response.xpath("//table/tr"):
            item = DoubanItem()
            item['title'] = i.css('a[class=nbg]::attr(title)').extract()[0].encode('utf-8')
            item['date'] = i.css('p[class="pl"]::text').extract()[0][:10].encode('utf-8')
            item['score'] = i.css('span[class="rating_nums"]::text').extract()[0].encode('utf-8')
            people = i.css('span[class="pl"]::text').extract()[0].encode('utf-8')

            item['people'] = filter(str.isdigit, people)

            print item
