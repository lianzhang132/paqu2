# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.files import FilesPipeline
from wangyi.settings import FILES_STORE as file_name
import os

class WangyiPipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        print("开始获取资源")
        # print(item)

        yield scrapy.Request(url=item["url"])

    def item_completed(self, results, item, info):
        # print(results)
        # 列表推导式
        song_name = item['song_name']
        old_name_list = [x['path'] for t, x in results if t]
        old_name = file_name + old_name_list[0]  # 真正的原图片的存储路径
        # print(old_name)
        # 判断图片存放的目录是否存在
        image_path = file_name
        if not os.path.exists(image_path):
            # 根据当前页码创建对应的目录
            os.mkdir(image_path)
        # # # 新名称 = images/1/sdfdfdf.jpg
        new_name = image_path + song_name + ".mp3"
        print("开始改名吧"+song_name)
        #     # print(page)
        # # 重命名
        os.rename(old_name, new_name)
        # print(old_name)
        # print("-------------------")
        # print(new_name)
        return item
