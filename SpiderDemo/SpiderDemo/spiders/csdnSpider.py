# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest
from  ..items import scdnspiderItem
# 多个爬虫用同一个item的操作 ====custom_settings
class CsdnspiderSpider(scrapy.Spider):
    name = 'csdnSpider'
    custom_settings = { 'ITEM_PIPELINES': {'SpiderDemo.pipelines.csdnSpiderpipne':50}}
    allowed_domains = ['cn.vuejs.org']
    start_urls = ['https://cn.vuejs.org/v2/guide/routing.html']
    # login_url='https://passport.csdn.net/login?code=public'
    # def start_requests(self):
    #     yield scrapy.Request(self.start_urls,callback=self.login)
    # def login(self,response):
    #     yield FormRequest.from_response(response,callback = self.parse)
    def parse(self, response):
        aimdata=response.css('.headerlink')
        for aimdata_detail in aimdata:
            item=scdnspiderItem()
            item['title']=aimdata_detail.css('.headerlink')
            yield item


