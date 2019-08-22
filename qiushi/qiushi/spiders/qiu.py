# -*- coding: utf-8 -*-
import scrapy
from qiushi.items import QiushiItem

class QiuSpider(scrapy.Spider):
    name = 'qiu'
    # allowed_domains = ['www.qiushibaike.com/text']
    start_urls = ['http://www.qiushibaike.com/text/']
    base_url = 'https://www.qiushibaike.com'

    def parse(self, response):
        item=QiushiItem()
        con_list=response.xpath('//div[@id="content-left"]/div')
        for con in con_list:
            item["name"]=con.xpath('./div/a[2]/h2/text()').extract_first()
            content=con.xpath('./a/div/span[1]/text()').extract()
            content="".join(content)
            item["content"]=str(content).strip()
            yield item

        next_url=response.xpath('//*[@id="content-left"]/ul/li[last()]/a/@href')
        if next_url:
            next_url1= self.base_url+next_url.extract_first()
            print("开始获取下一页")
            yield scrapy.Request(url=next_url1,callback=self.parse)



