# -*- coding: utf-8 -*-
import scrapy
from wangyi.items import WangyiItem

class YinyueSpider(scrapy.Spider):
    name = 'yinyue'
    allowed_domains = ['music.163.com/#/playlist?id=2925655176']
    start_urls = ['https://music.163.com/playlist?id=2925655176']

    def parse(self, response):


        lis=response.xpath('//ul[@class="f-hide"]/li')
        base_url = 'https://link.hhtjim.com/163/'
        # print(lis)
        # file_urls = []
        for li in lis:
            item = WangyiItem()
            item["song_name"] = li.xpath('./a/text()')[0].get()
            song_url = li.xpath('./a/@href')[0].get()

            # print(song_url,item["song_name"])

            song_id = song_url.split('=')[-1]
            item["url"]=base_url+song_id+'.mp3'
            # file_urls.append(base_url+song_id+'.mp3')
            print(item["song_name"]+"可以下载了")
            # print(song_id)
            print(item)
            yield item

    # def detailparse(self,response,item):

