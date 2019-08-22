# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from fuli.items import FuliItem

class XiezhenSpider(CrawlSpider):
    name = 'xiezhen'
    # allowed_domains = ['www.okzy.co/?m=vod-type-id-22.html']
    start_urls = ['http://www.okzy.co/?m=vod-type-id-22.html']
    link=LinkExtractor(allow=r'/?m=vod-type-id-22-pg-\d{0,2}.html')
    rules = (
        Rule(link, callback='parse_item', follow=True),
    )
    def parse_item(self, response):
        # print(response)
        # xpath插件中的数字下标  会影响到代码中的取值  此时ul_list是每个页面中的链接列表
        ul_list = response.xpath('//div/ul/li/span[2]/a/@href').extract()
        # print(ul_list)
        base_url="http://www.okzy.co/"
        for ul in ul_list:
            url=base_url+ul
            yield scrapy.Request(url=url, callback=self.detailParse)

    def detailParse(self,response):
        item = FuliItem()
        item["title"] = response.xpath("//div/div[1]/div/div/div[2]/div[1]/h2/text()").extract_first()
        item["plaradd"] = response.xpath('//*[@id="1"]/ul/li/text()').extract_first()
        item["downlodd"] = response.xpath('//*[@id="down_1"]/ul/li/text()').extract_first()
        yield item

