# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Job51Item(scrapy.Item):
    # define the fields for your item here like:
    company = scrapy.Field()
    workname = scrapy.Field()
    salary = scrapy.Field()
    add = scrapy.Field()
    workdetail = scrapy.Field()
    require = scrapy.Field()
    # add = scrapy.Field()

