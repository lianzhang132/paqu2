# -*- coding: utf-8 -*-
import scrapy
import json

class KfcaddSpider(scrapy.Spider):
    name = 'kfcadd'
    # allowed_domains = ['www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname']
    start_urls = ['http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname']

    def start_requests(self):
        print("开始查找")
        data = {
            'cname': '上海',
            'pid':'',
            'pageIndex': '2',
            'pageSize': '10',
            # 'keyword':''

        }
        for url in self.start_urls:
            yield scrapy.FormRequest(url=url, callback=self.parse, formdata=data)

    def parse(self, response):
        # print(111)
        data=json.loads(response.text)
        # print(data)
        resu=data["Table1"]

        # print(resu)
        # exit()
        for da in resu:
            print(da['storeName'], da['addressDetail'])
