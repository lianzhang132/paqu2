# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from job51.items import Job51Item

class PyjobsSpider(CrawlSpider):
    name = 'pyjobs'
    # allowed_domains = ['https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c']
    start_urls = ['https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html']
    link=LinkExtractor(allow=r'https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,\d+.html')
    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        joburl_list = response.xpath('//*[@id="resultList"]/div/p/span/a/@href').extract()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # print(joburl_list)
        # print(len(joburl_list))
        for job in joburl_list:
            # print(job)
            yield scrapy.Request(url=job, callback=self.detailParse)

        # print(len(joburl_list))
    def detailParse(self,response):
        item = Job51Item()
        print("可以获取详情了")
        # print(response)
        item['company'] = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[1]/a[1]/@title').extract_first()
        if not item['company']:
            item['company'] = "暂无"
        item['workname'] = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/h1/@title').extract_first()
        if not item['workname']:
            item['workname'] = "暂无"
        item['salary'] = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/strong/text()').extract_first()
        if  not item['salary']:
            item['salary']="暂无"
        # print(item['salary'])
        item['add'] = response.xpath('/html/body/div[3]/div[2]/div[3]/div[2]/div/p/text()').extract_first()
        if  not item['add']:
            item['add']="暂无"

        item['workdetail'] = "".join(response.xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div/p/text()').extract())
        if not item['workdetail']:
            item['workdetail'] = "暂无"
        item['require'] = "".join(response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()').extract())
        if not item['require']:
            item['require'] = "暂无"
        yield item