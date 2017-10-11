import scrapy
import json
from douban.items import ZhihuItem

class ZhiHu(scrapy.Spider):
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    # top-level root topic
    top_topic = 'https://www.zhihu.com/topic/19618774/top-answers'

    start_urls = [top_topic]

    def login(self, response):
        _xsrf = response.xpath('//div[@data-za-module="SignInForm"]/form/input[@name="_xsrf"]/@value').extract()[0]
        captcha = response.xpath('//div[@data-za-module="SignInForm"]/form/div/div/div/input[@name="captcha"]/@type').extract()[0].encode('utf-8')
        if('hidden' == captcha):
            print 'do not need captcha'
        account = 'achen_5@163.com'
        pwd = '123456a'
        data = {'_xsrf': _xsrf, 'email': account, 'password': pwd,'captcha_type':'cn'}
        # url = {'url':"https://www.zhihu.com/login/email"}
        yield scrapy.FormRequest.from_response(response, formdata=data, callback=self.after_login,formxpath='//div[@data-za-module="SignInForm"]/form',url = "https://www.zhihu.com/login/email")

    def after_login(self, response):
        resp = json.loads(response.body)
        print resp['msg'].encode('utf-8')
        # if 100000 == resp['errcode']:
        #     self.logger.error("Login failed")
        #     return

    # def start_requests(self):
    #     yield scrapy.Request('https://www.zhihu.com/', callback=self.login)

    def parse(self, response):

        for i in response.xpath('//div[@id="zh-topic-top-page-list"]/div[@itemprop="question"]'):
            item = ZhihuItem()
            answer_url = i.xpath('.//link/@href').extract()[0]
            ques = i.xpath('.//div/h2/a/text()').extract()[0].encode('utf-8')
            author = i.xpath('.//span[@class="author-link-line"]/a')
            if author :
                author = i.xpath('.//span[@class="author-link-line"]/a/text()').extract()[0].encode('utf-8')
                author_url = i.xpath('.//span[@class="author-link-line"]/a/@href').extract()[0]
                item['author'] = author
                item['author_url'] = author_url
            item['answer_url']=answer_url
            item['question'] = ques

            yield item
        next_url = response.xpath('//div[@class="zm-invite-pager"]/span/a/@href').extract()[-1]

        yield scrapy.Request(next_url)
        print next_url




    def parseChildTopic(self, response):

        for i in response.xpath('//div[@class="zm-side-section-inner child-topic"]/div/a'):
            child_topic_url = i.xpath('@href').extract()[0]
            child_topic_name = i.xpath('text()').extract()[0].encode('utf-8')

            print child_topic_url,child_topic_name