# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class SpiderdemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    goodimg=scrapy.Field()
    goodName=scrapy.Field()

class scdnspiderItem(scrapy.Item):
     title=scrapy.Field()
     content=scrapy.Field()

class scdnlogiItem(scrapy.Item):
     title=scrapy.Field()
     title_href=scrapy.Field()
     content=scrapy.Field()
     make_time=scrapy.Field()
     Art_reder=scrapy.Field()
