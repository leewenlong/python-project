# -*- coding: utf-8 -*-

import scrapy
from douban.items import TvItem
import json


class TvTop(scrapy.Spider):
    name = "tvtop"
    allowed_domains = ["movie.douban.com"]
    start_urls = ['https://movie.douban.com/j/search_subjects?type=tv&tag=国产剧&sort=rank&page_limit=20&page_start=0']

    start = 1

    def parse(self, response):
        body = json.loads(response.body)
        for i in body['subjects']:
            url = i['url']
            yield scrapy.Request(url, callback=self.parseDetail)

        next_url = "https://movie.douban.com/j/search_subjects?type=tv&tag=国产剧&sort=rank&page_limit=20&page_start=" + str(
            self.start)
        self.start += 1

        yield scrapy.Request(next_url)

    def parseDetail(self, response):
        # print response.body
        item = TvItem()
        item['title'] = response.xpath('//span[@property="v:itemreviewed"]/text()').extract()[0]
        item['score'] = response.xpath('//div[@class="rating_self clearfix"]/strong/text()').extract()[0].encode(
            "utf-8")
        item['people'] = response.xpath('//a[@class="rating_people"]/span/text()').extract()[0]
        year = response.xpath('//h1/span[@class="year"]/text()').extract()[0]
        item['year'] = filter(str.isdigit, year.encode("utf-8"))

        yield item
