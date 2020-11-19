# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.dirname(__file__) + os.sep + '../')
# from ..SpiderDemo import spiders
# Scrapy settings for SpiderDemo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'SpiderDemo'

SPIDER_MODULES = ['SpiderDemo.spiders']
NEWSPIDER_MODULE = 'SpiderDemo.spiders'
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'Host':'b2b.baidu.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'SpiderDemo (+https://b2b.baidu.com/)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# 同时启动多个spider
# COMMANDS_MODULE=spiders.commands
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16
# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   'SpiderDemo.middlewares.SpiderdemoSpiderMiddleware': 543,
    "scrapy.downloadermiddlewares.redirect.RedirectMiddleware":600,
   "scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware":580,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'SpiderDemo.middlewares.SpiderdemoDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}
# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'SpiderDemo.pipelines.SpiderdemoPipeline': 300,
    'SpiderDemo.pipelines.SpiderdemoPipeline_mogodb':200,
    'SpiderDemo.pipelines.SpiderdemoPipeline_Redis':100,
}

#将数据存储在mysql中的配置
MYSQL_HOST = '192.168.1.123'
MYSQL_DBNAME = 'spiderData'
MYSQL_USER = 'root'
MYSQL_PASSWD = '123456'
MYSQL_PROT = 3306
MYSQL_charset = 'utf8'
MYSQL_use_unicode = True

#mogodb
Mogodb_url='mongodb://localhost:27017'
Mogodb_DB='mogSpiderdb'
MONGO_COLL ='mogSpiderdb'
#redis
Redis_host='127.0.0.1'
Redis_indenx_DB=0

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
LOG_LEVEL= 'DEBUG'
HTTPERROR_ALLOWED_CODES = [302]

#分布式搭建————优化
# 使用scrapy_redis的去重类 不使用scrapy默认的去重类
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用scrapy_redis的调度器 不使用scrapy默认的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 控制爬虫是否允许暂停
SCHEDULER_PERSIST = True