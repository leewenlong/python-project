# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    title = scrapy.Field()
    score = scrapy.Field()
    people = scrapy.Field()
    date = scrapy.Field()


class TvItem(scrapy.Item):
    title = scrapy.Field()
    score = scrapy.Field()
    people = scrapy.Field()
    year = scrapy.Field()


class ZhihuItem(scrapy.Item):
    answer_url = scrapy.Field()
    question = scrapy.Field()
    author = scrapy.Field()
    author_url = scrapy.Field()
    _id = scrapy.Field()

