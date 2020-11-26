import os

from django.shortcuts import render
# Create your views here.
import requests
import base64

from pythonstudio import STATICFILES_DIRS

'''通用文字识别（高精度版）'''
def  ataintocke():
  AK='MOLpEoO3vcBHA0yMHidLrRNE'
  SK='A11UNvGFMsEyeLoIbGX6G6d5jVbkvQDW'
  host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={AK}&client_secret={SK}'.format(AK=AK,SK=SK)
  response = requests.get(host)
  return response.json()['access_token']
def getFilePath(filepath):
   with open(filepath,'rb') as p:
       f=p.read()
   return f
def construe(imgfile):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    # 二进制方式打开图片文件
    f = getFilePath(filepath=imgfile)
    img= base64.b64encode(f)
    params = {"image": img}
    access_token = ataintocke()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    word_content_result=[]
    for i in  response.json()['words_result']:
        word_content=i['words']
        word_content_result.append(word_content)
    return word_content_result
# 实现上传图片功能
def index(request):
    if request.method=='GET':
      return  render(request,'index.html')
    if request.method=="POST":
        filename=request.FILES.get('filename')
        path = os.path.join(STATICFILES_DIRS[0], 'img')
        if filename:
          with open(os.path.join(path,filename.name),'wb')as f:
            for i in filename.chunks():
               f.write(i)
        return  render(request,'index.html')

