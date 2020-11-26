# from django.test import TestCase
#
# # Create your tests here.
#
#
# import requests
# import base64
# '''
# 通用文字识别（高精度版）
# '''
# def  ataintocke():
#   AK='MOLpEoO3vcBHA0yMHidLrRNE'
#   SK='A11UNvGFMsEyeLoIbGX6G6d5jVbkvQDW'
#   host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={AK}&client_secret={SK}'.format(AK=AK,SK=SK)
#   response = requests.get(host)
#   return response.json()['access_token']
# def getFilePath(filepath):
#    with open(filepath,'rb') as p:
#        f=p.read()
#    return f
# def construe(imgfile):
#     request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
#     # 二进制方式打开图片文件
#     f = getFilePath(filepath=imgfile)
#     img= base64.b64encode(f)
#     params = {"image": img}
#     access_token = ataintocke()
#     request_url = request_url + "?access_token=" + access_token
#     headers = {'content-type': 'application/x-www-form-urlencoded'}
#     response = requests.post(request_url, data=params, headers=headers)
#     word_content_result=[]
#     for i in  response.json()['words_result']:
#         word_content=i['words']
#         word_content_result.append(word_content)
#     return word_content_result
# if __name__=="__main__":
#    op=construe(imgfile='D:\\新媒体包\\新媒体内容\\压脚图书\\个人成长\\图片\\图片11\\6.jpg')
#    result=''.join(op).replace(',','\n')
#    print(result)




# import  numpy
#
# a=numpy.arange(15).reshape(3,5)
# print(a)
#
# b=numpy.array([[1,3,5,6],[7,8,9,10]],dtype=complex)
# print(b)

# 数据分析 人工智能 词云
import os
import time
import  jieba
from   matplotlib import pyplot as plt
from  wordcloud import WordCloud
from  PIL import Image
import  numpy as np

import pandas as pd
s=pd.Series([27.2,12,58,69,54])
print(s)











# df=pd.read_csv('D:\\Downloads\\Combined_News_DJIA.csv',header=None,error_bad_lines=False,encoding='utf-8')
# data=df.head()
# print(data)
# pt2=pd.pivot_table(data,index=['股票数据'],columns=['股票描述'])
# print(pt2)
# from multiprocessing import  Process,Pool
# # 自定义进程
# class myprocess(Process):
#     def run(self):
#         print('自定义进程.....')
#
# def task(s,name):
#     while True:
#         time.sleep(2)
#         print('1')
#
# def task1(s,name):
#     while True:
#         time.sleep(2)
#         print('2')
# # import  threading
# # def sayhellow(num):
# #     time.sleep(3)
# if __name__=="__main__":
#     pidentifie=myprocess()
#     pidentifie.run()
#     p=Process(target=task,name='任务一',args=(4,'aa'))
#     p.start()
#     p = Process(target=task1, name='任务一', args=(2,'bb'))
#     p.start()

    # t1=threading.Thread(target=sayhellow,args=(1,))
    # t2=threading.Thread(target=sayhellow,args=(2,))
    # t1.start()
    # t2.start()
    #
    # print(t1.getName())
    # print(t2.getName())


#装饰器
# def decration(func):
#     a=100
#     def wrapper(*args,**kwargs ):
#         print('''开始执行装饰器中的函数''')
#         func()
#         print('''装饰器中函数执行结束''')
#     return  wrapper()
# @decration
# def f1(name='张三'):
#     print('开始执行被装饰的函数'+name)




