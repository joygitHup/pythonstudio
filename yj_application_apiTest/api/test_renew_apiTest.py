import json
import logging
import unittest
import requests
from yj_application_apiTest.config import httpConfig
from yj_application_apiTest.otherFile.test import test_loginApicase1
from yj_application_apiTest.tools.logClas import MyLog

class test_renew_apitest(unittest.TestCase):
    def setUp(self):
        pass
    def test_rebuited_worksheet(self):
        url = httpConfig.host1 + httpConfig.new_rebuited_data_url
        # data = httpConfig.dataUploa
        headers = httpConfig.headers
        headers['Authorization'] = 'JWT ' + test_loginApicase1()
        re = requests.put(url, headers=headers, verify=False)
        result = re.status_code
        # 添加断言
        print(result)
    def tearDown(self):
        pass
if __name__=="__main__":
  unittest.main()