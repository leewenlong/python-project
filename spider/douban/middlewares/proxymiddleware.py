# -*- coding: utf-8 -*-
from fake_useragent import UserAgent


class ProxyMiddleware:
    def process_request(self, request, spider):
        ua = UserAgent()
        # request.meta["proxy"] = "http://10.128.7.118:8087"
        # request.headers.setdefault('User-Agent', ua['random'])  # 添加随机出来的user-agent
