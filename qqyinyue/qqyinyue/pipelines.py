# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class QqyinyuePipeline(object):
    conn = None
    mycursor = None
    def open_spider(self,spider):
        print("开始采集")
        self.conn=pymysql.connect(host="localhost",user="root",password="666666",db="xima",port=3306)
        # 获取游标
        self.mycursor = self.conn.cursor()
    def process_item(self, item, spider):
        print("写入中")
        name = item["name"]
        url = item["url"]
        sql="insert into fmmusic VALUES (null,'%s','%s')"%(name,url)

        boo= self.mycursor.execute(sql)
        self.conn.commit()

        return item


    def close_spider(self,spider):
        print("结束了")
        self.mycursor.close()
        self.conn.close()

