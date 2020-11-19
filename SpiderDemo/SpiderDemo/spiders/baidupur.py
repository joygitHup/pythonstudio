# -*- coding: utf-8 -*-
from base64 import decode
from urllib.parse import unquote
import scrapy
from urllib import parse
from  ..items import SpiderdemoItem

class BaidupurSpider(scrapy.Spider):
    name = 'baidupur'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/']

    # start_urls = []
    # keyword =input('请输入你要采集数据的关键词：')
    # url = "https://b2b.baidu.com/xx"
    # xx = "s?q={}&from=search".format(unquote(keyword))
    # urljoin = parse.urljoin(url,xx)
    # start_urls.append(unquote(urljoin))
    def parse(self, response):
        #getall()  == extract()
        extra_content=response.css('.s-top-left')
            # css('.main-content').extract()
        print(extra_content)
        for item_details in extra_content:
            # print(item_details)
            item=SpiderdemoItem()
            # goodimg=item_details.css(".name>span").extract()
            goodimg=item_details.xpath('//*[@id="s-top-left"]/a/@href').extract()
            goodName=item_details.xpath('//*[@id="s-top-left"]/a/text()').extract()
            item['goodimg']=goodimg[0]
            item['goodName']=goodName[0]
            yield  item
        # 翻页功能的实现
        # if self.offset <= 5:
        #     self.offset += 1
        #     url = self.baseURL + str(self.offset)
        #     yield scrapy.Request(url, callback=self.parse)
