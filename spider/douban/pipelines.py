# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import douban.Mysql as mysql
import douban.mongo as mongo


class DoubanPipeline(object):
    def process_item(self, item, spider):
        return item


class ZhihuMongoPipeline(object):
    def process_item(self, item, spider):
        mongo.insert(mongo.conn(), item)
        return item


class ZhihuMySQLPipeline(object):
    def process_item(self, item, spider):
        mysql.insert(item)
        return item
