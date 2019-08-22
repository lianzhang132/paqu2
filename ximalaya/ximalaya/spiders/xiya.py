# -*- coding: utf-8 -*-
import scrapy
from ximalaya.items import  XimalayaItem

class XiyaSpider(scrapy.Spider):
    name = 'xiya'
    # allowed_domains = ['www.ximalaya.com/yinyue/3595841/']
    start_urls = ['http://www.ximalaya.com/yinyue/3595841/']

    def parse(self, response):
        # file_path = './music/'
        # if not os.path.exists(file_path):
        #     os.mkdir(file_path)

        div_list = response.xpath('//*[@id="anchor_sound_list"]/div[2]/ul/li/div[2]')
        base_url = "https://link.hhtjim.com/ximalaya/"
        for div in div_list:
            items = XimalayaItem()
            name = div.xpath("./a/@title").extract_first() + ".mp3"
            items["name"] = div.xpath("./a/@title").extract_first() + ".mp3"
            url_id = div.xpath("./a/@href").extract_first().split("/")[-1]
            url = base_url + url_id + ".mp3"
            items["url"] = base_url + url_id + ".mp3"
            # res=requests.get(url=url).content
            # dic = {
            #     "name": name,
            #     "url": url
            # }
            # with open(file_path+name, 'wb') as f:
            #     f.write(res)
            #     print('%s下载成功' % name)
            yield items
