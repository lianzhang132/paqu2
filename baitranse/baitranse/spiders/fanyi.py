# -*- coding: utf-8 -*-
import scrapy
import json


class FanyiSpider(scrapy.Spider):
    name = 'fanyi'
    allowed_domains = ['fanyi.baidu.com/sug']
    start_urls = ['http://fanyi.baidu.com/sug/']

    def start_requests(self):
        print("开始翻译")
        data = {
            "kw":"开始"
        }
        for url in self.start_urls:
            yield scrapy.FormRequest(url=url,callback=self.parse,formdata=data)

    def parse(self, response):
        # print(111)
        data=json.loads(response.text)
        # print(data)
        resu=data["data"]
        # print(resu)
        # exit()
        for da in resu:
            print(da['k'], da['v'])


