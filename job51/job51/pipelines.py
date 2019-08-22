# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
class Job51Pipeline(object):
    f = None

    def open_spider(self, spider):
        self.f = open("上海python.txt", 'w', encoding="utf-8")

    def process_item(self, item, spider):
        print("开始保存")
        time.sleep(3)
        print(item['workname'])
        self.f.write(item['company']+item['workname']+item['salary']+item['require']+item['add']+"\n\n"+
                    item['workdetail']+"\n\n\n\n\n\n")
        return item
    def close_spider(self, spider):
        self.f.close()

