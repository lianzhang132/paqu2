# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis
import pymysql

class XimalayaPipeline(object):
    conn = None
    mycursor = None

    def open_spider(self, spider):
        print("开始采集")
        self.conn = pymysql.connect(host="localhost", user="root", password="666666", db="xima", port=3306)
        # 获取游标
        self.mycursor = self.conn.cursor()

    def process_item(self, item, spider):
        print("写入中")
        name = item["name"]
        url = item["url"]
        sql = "insert into fmmusic VALUES (null,'%s','%s')" % (name, url)

        boo = self.mycursor.execute(sql)
        self.conn.commit()

        return item

    def close_spider(self, spider):
        print("结束了")
        self.mycursor.close()
        self.conn.close()
class FilePipeline(object):
    f = None
    def open_spider(self, spider):
        print("开始采集")
        self.f = open("xima.txt","w", encoding="utf-8")


    def process_item(self, item, spider):
        print("写入中")
        name = item["name"]
        url = item["url"]
        self.f.write(name+":"+url+"\n\n")


    def close_spider(self, spider):
        print("结束了")
        self.f.close()


class RedisPipeline(object):
    r = None


    def open_spider(self, spider):
        print("开始采集")
        self.r = redis.Redis(host="127.0.0.1",port=6379,password="123456",db=0)


    def process_item(self, item, spider):
        print("写入中")
        name = item["name"]
        url = item["url"]
        dic = {
            "name": name,
            "url": url
        }
        self.r.lpush("con",dic)
        return item

    def close_spider(self, spider):
        print("结束了")
        self.r.close()




