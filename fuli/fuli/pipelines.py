# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


# class FuliPipeline(object):
#     def process_item(self, item, spider):
#         return item

class FuliPipeline(object):
    conn=None
    mycursor=None
    def open_spider(self,spider):
        print("数据库开始链接")
        self.conn=pymysql.connect(host="127.0.0.1",user="root",password="666666",db="xima",port=3306)


    def process_item(self, item, spider):

        self.mycursor=self.conn.cursor()
        sql="insert into fuli VALUES (null,'%s','%s','%s')"%(item['title'],item['plaradd'],item['downlodd'])
        self.mycursor.execute(sql)
        self.conn.commit()
        print("插入一条成功。。。")
        return item
    def  close_spider(self,spider):
        print("数据库断开")
        self.mycursor.close()
        self.conn.close()

