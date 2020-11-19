import json
import logging
import unittest
import requests
from yj_application_apiTest.config import httpConfig
from yj_application_apiTest.config.pathconfig import casefilePath
from yj_application_apiTest.tools.logClas import MyLog
from yj_application_apiTest.tools.readExcel import openSheet


class Test_login(unittest.TestCase):
  '''用户登录'''
  def setup(self):
     print("-----start----")
  def test_loginApicase1(self):
    # logging.captureWarnings(True)
    MyLog.info("开始:{}".format('测试登录接口'))
    url=httpConfig.host+httpConfig.wholeURl
    data=httpConfig.data1
    headers=httpConfig.headers
    re=requests.post(url,data=data,headers=headers,verify=False)
    recode=re.status_code
    result=json.loads(re.text)
    #添加断言
    self.assertEqual(200,recode)
    self.assertTrue('token'in re.text)
    return result['token']
  def test_loginApicase_Allerro(self):
    # logging.captureWarnings(True)
    MyLog.info("开始:{}".format('测试登录接口_'+'账户名和用户名都错误的用例'))
    url=httpConfig.host+httpConfig.wholeURl
    data=httpConfig.data2
    headers=httpConfig.headers
    re=requests.post(url,data=data,headers=headers,verify=False)
    recode=re.status_code
    result=json.loads(re.text)
    #添加断言
    self.assertEqual(599,recode)

  def test_loginApicase_username_erro(self):
    # logging.captureWarnings(True)
    MyLog.info("开始:{}".format('测试登录接口_'+'账户名和用户名都错误的用例'))
    url=httpConfig.host+httpConfig.wholeURl
    data=httpConfig.data3
    headers=httpConfig.headers
    re=requests.post(url,data=data,headers=headers,verify=False)
    recode=re.status_code
    result=json.loads(re.text)
    #添加断言
    self.assertEqual(200,recode)

  def test_loginApicase_pwd_erro(self):
    # logging.captureWarnings(True)
    MyLog.info("开始:{}".format('测试登录接口_'+'账户名和用户名都错误的用例'))
    url=httpConfig.host+httpConfig.wholeURl
    data=httpConfig.data4
    headers=httpConfig.headers
    re=requests.post(url,data=data,headers=headers,verify=False)
    recode=re.status_code
    result=json.loads(re.text)
    #添加断言
    self.assertEqual(599,recode)
  def tearDown(self):
     print('-----end------')


# 通过数据表格管理用例
class Test_login2(unittest.TestCase):
   '''数据表格管理用例_登录测试用例'''
   def setUp(self):
       pass
   def test_loginApicase1(self):
       MyLog.info("开始:{}".format('测试登录接口'))
       url = httpConfig.host + httpConfig.wholeURl
       data = openSheet(filepath=casefilePath,clo=9,row=2)
       headers = httpConfig.headers
       re = requests.post(url, data=data, headers=headers, verify=False)
       recode = re.status_code
       result = json.loads(re.text)
       self.assertEqual(300, recode)
       self.assertTrue('token' in re.text)
       # 添加断言
       # try:
       #
       # except AssertionError as e:
       #    print(e)
       return result['token']
   def tearDown(self):
       pass



def  upload_file():
    MyLog.info("开始:{}".format('上传接口_' + '账户名和用户名都错误的用例'))
    url = httpConfig.host + httpConfig.wholeURl_upload
    data = httpConfig.dataUploa
    headers = httpConfig.headers
    re = requests.post(url, data=data, headers=headers, verify=False)
    # recode = re.status_code
    # result = json.loads(re.text)
    # 添加断言
    print(re)

def rebuid_member_a_list():
    logging.captureWarnings(True)
    url = httpConfig.host + 'desktop/inspection_sheets/field_values/?page=1&page_size=100'
    data = {"keyword":"","field_key":"member_a"}
    headers = httpConfig.headers
    headers['Authorization']='JWT '+Test_login.test_loginApicase1()
    re = requests.post(url, data=data, headers=headers, verify=False)
    result = json.loads(re.text)
    return result
def  rebuid_work_category_list():
    logging.captureWarnings(True)
    url = httpConfig.host + 'desktop/inspection_sheets/field_values/'
    data = {"keyword":"","field_key":"work_category"}
    headers = httpConfig.headers
    headers['Authorization'] = 'JWT ' + loginApi()
    print(headers)
    re = requests.post(url, data=data, headers=headers, verify=False)
    result = json.loads(re.text)
    print(result)
    return result
def rebuid_work_category_content_lsits():
    logging.captureWarnings(True)
    url = httpConfig.host + 'desktop/inspection_sheets/field_values/'
    data = {"keyword":"","field_key":"work_content","work_category":"c38dcb34-eec9-11ea-8f22-38f9d355d676"}
    headers = httpConfig.headers
    headers['Authorization'] = 'JWT ' + loginApi()
    re = requests.post(url, data=data, headers=headers, verify=False)
    result = json.loads(re.text)
    print(result)
    return result
def rebuid_work_resources_uploadsignature():
    logging.captureWarnings(True)
    url = httpConfig.host + 'desktop/inspection_sheets/field_values/'
    data = {"type":200,"extension":"jpg"}
    headers = httpConfig.headers
    headers['Authorization'] = 'JWT ' + loginApi()
    files = {"file": ("10.jpg", open("D:\\Pictures\\10.jpg", "rb"), "image/jpeg", {})}
    data['files']=data
    re = requests.post(url, data=data, headers=headers, verify=False)
    result = json.loads(re.text)
    return result

def rebuiding_work():
    # desktop / inspection_sheets /stages/
    logging.captureWarnings(True)
    url = httpConfig.host + 'desktop/inspection_sheets/stages/'
    data = {
            "stages":[
                {"work_id":"09-24",
                 "str_datetime":1602659950520,
                 "end_datetime":1602919152897,
                 "member_a":"dv1","member_b":"dv2",
                 "member_c":"dv2","member_d":"driver1",
                 "member_e":"dv2",
                 "work_category":"c38dcb34-eec9-11ea-8f22-38f9d355d676",
                 "work_content":"da8365d8-eec9-11ea-944d-38f9d355d676",
                 "initial_remark":[],"stage":"0"}]}
    headers = httpConfig.headers
    headers['Authorization'] = 'JWT ' + loginApi()
    re = requests.post(url, json=data, headers=headers, verify=False)
    result = json.loads(re.text)
    print(result)
    return result
def pepole_list():
    logging.captureWarnings(True)
    url = httpConfig.host + 'admin/users/?page=1&page_size=10'
    # data = {"keyword": "", "field_key": "work_content", "work_category": "c38dcb34-eec9-11ea-8f22-38f9d355d676"}
    headers = httpConfig.headers
    headers['Authorization'] = 'JWT ' + loginApi()
    re = requests.get(url,  headers=headers, verify=False)
    result = json.loads(re.text)
    print(result)
    return result
def pepole_list_secher():
    logging.captureWarnings(True)
    url = httpConfig.host + 'admin/users/?user__username__icontains=wang'
    # data = {"keyword": "", "field_key": "work_content", "work_category": "c38dcb34-eec9-11ea-8f22-38f9d355d676"}
    headers = httpConfig.headers
    headers['Authorization'] = 'JWT ' + loginApi()
    re = requests.get(url,  headers=headers, verify=False)
    result = json.loads(re.text)
    print(result)
    return result
def pepole_list_Add():
    logging.captureWarnings(True)
    url = httpConfig.host + 'admin/signup/'
    # data = {"keyword": "", "field_key": "work_content", "work_category": "c38dcb34-eec9-11ea-8f22-38f9d355d676"}
    data = {"username": "自动化测试", "password": "ceshi123456"}
    headers = httpConfig.headers
    headers['Authorization'] = 'JWT ' + loginApi()
    re = requests.post(url,data=data,headers=headers,verify=False)
    # result = json.loads(re.text)
    # print(result)
    print(re)
    # return result
if __name__=="__main__":
  unittest.main()

# 上传文件接口 测试的demo
#









