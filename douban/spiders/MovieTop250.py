import scrapy
from douban.items import DoubanItem


class Top250(scrapy.Spider):
    name = "top250"
    allowed_domains = ["movie.douban.com"]
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        # print response.body
        for i in response.xpath("//ol/li"):
            item = DoubanItem()
            item['title'] = i.xpath('.//div[@class="hd"]/a/span/text()').extract()[0].encode("utf-8")

            item['score'] = i.xpath('.//span[@class="rating_num"]/text()').extract()[0].encode("utf-8")
            people  = i.xpath('.//div[@class="bd"]/div/span/text()').extract()[1].encode("utf-8")
            item['people'] = filter(str.isdigit, people)

            print item
            pass  #待完成
