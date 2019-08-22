# -*- coding: utf-8 -*-
import scrapy


class PyjobSpider(scrapy.Spider):
    name = 'pyjob'
    # allowed_domains = ['https://search.51job.com/list/170200%252C040000%252C010000%252C02000']
    start_urls = ['https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    def parse(self, response):
        joblist=response.xpath('//*[@id="resultList"]/div/p/span/a/@href')
        for job in joblist:
            yield scrapy.Request()
