# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sys,os

import pymongo
import redis

sys.path.append(os.path.dirname(__file__) + os.sep + '../')
import pymysql
from SpiderDemo import settings

class SpiderdemoPipeline:
    def __init__(self):
        self.connectdb=pymysql.Connect(host=settings.MYSQL_HOST,port=settings.MYSQL_PROT
                                       ,db=settings.MYSQL_DBNAME,user=settings.MYSQL_USER,
                                       password=settings.MYSQL_PASSWD,use_unicode=settings.MYSQL_use_unicode
                                       ,charset=settings.MYSQL_charset
                                       )
        self.curous=self.connectdb.cursor()
    def process_item(self, item, spider):
        self.curous.execute("insert into  baiduTable (name ,nameurl)values(%s,%s)",(item['goodName'],item['goodimg']))
        self.connectdb.commit()
        return item
    def close_connectdb(self):
        self.curous.close()
        self.connectdb.close()

class SpiderdemoPipeline_mogodb:
    def __init__(self):
        self.client = pymongo.MongoClient(host=settings.Mogodb_url)
        self.db =self.client[settings.Mogodb_DB]  # 获得数据库的句柄
        self.coll = self.db[settings.MONGO_COLL]  # 获得collection的句柄
        # 数据库登录需要帐号密码的话
        # self.db.authenticate(settings['MONGO_USER'], settings['MONGO_PSW'])
    def process_item(self, item, spider):
        postItem = dict(item)  # 把item转化成字典形式
        self.coll.insert(postItem)  # 向数据库插入一条记录
        return item  # 会在控制台输出原item数据，可以选择不写

class SpiderdemoPipeline_Redis:
    def __init__(self):
        self.con_redis=redis.StrictRedis(host=settings.Redis_host,db=settings.Redis_indenx_DB)
    def process_item(self, item, spider):
        self.con_redis.rpush('url',item['goodimg']) # 向数据库插入一条记录（url为key  item['goodimg']为值）
        return item  # 会在控制台输出原item数据，可以选择不写
    def close_con_redis(self):
        self.con_redis.connection_pool.disconnect()


class csdnSpiderpipne:
    pass