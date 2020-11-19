
# from yj_application_apiTest.tools.logClas import MyLog
import json
import requests
from yj_application_apiTest.config import httpConfig
def test_loginApicase1():
    # logging.captureWarnings(True)
    url = httpConfig.host + httpConfig.wholeURl
    data = httpConfig.data1
    headers = httpConfig.headers
    re = requests.post(url, data=data, headers=headers, verify=False)
    recode = re.status_code
    result = json.loads(re.text)
    return result['token']
def  upload_file_data():
    # MyLog.info("开始:{}".format('上传接口_' + '账户名和用户名都错误的用例'))
    url = httpConfig.host1 + httpConfig.upload_file_data_url
    # data = httpConfig.dataUploa
    headers = httpConfig.headers
    headers['Authorization'] = 'JWT ' + test_loginApicase1()
    re = requests.put(url, headers=headers, verify=False)
    result = re.status_code
    # 添加断言
    print(result)
def new_rebuited_worksheet():
    url = httpConfig.host1 + httpConfig.new_rebuited_data_url
    # data = httpConfig.dataUploa
    headers = httpConfig.headers
    headers['Authorization'] = 'JWT ' + test_loginApicase1()
    re = requests.put(url, headers=headers, verify=False)
    result = re.status_code
    # 添加断言
    print(result)
def editor_userinfor():
    url = httpConfig.host+ httpConfig.editor_userinfor_host
    data =httpConfig.editor_userinfor_data
    headers = httpConfig.headers
    headers['Authorization'] = 'JWT ' + test_loginApicase1()
    re = requests.patch(url,data=data,headers=headers, verify=False)
    result = re.status_code
    # 添加断言
    print(result)
def work_setting_add_meterail():
    url = httpConfig.host + httpConfig.add_meterail_host
    data = httpConfig.add_meterail_data
    headers = httpConfig.headers
    headers['Authorization'] = 'JWT ' + test_loginApicase1()
    re = requests.post(url, data=data, headers=headers, verify=False)
    result = re.status_code
    # 添加断言
    print(result)
if __name__=="__main__":
    work_setting_add_meterail()





























# def  upload_file():
#     MyLog.info("开始:{}".format('上传接口_' + '账户名和用户名都错误的用例'))
#     url = httpConfig.host + httpConfig.wholeURl_upload
#     data = httpConfig.dataUploa
#     headers = httpConfig.headers
#     headers['Authorization'] = 'JWT ' + test_loginApicase1()
#     re = requests.post(url, data=data, headers=headers, verify=False)
#     # recode = re.status_code
#     # result = json.loads(re.text)
#     # 添加断言
#     return  re
#
# def upload_file_result():
#     pass
#     # 'admin/procedures/6bb9f788-cb02-11ea-a2d1-38f9d355d676/extends/?page=1&page_size=1000'
# if __name__=="__main__":
#     upload_file()
# import  matplotlib.pyplot as plt
# plt.plot([1,2,3],[4,5,3])
# plt.show()
#
# import pandas as  pd
# import numpy as np
# pf=pd.DataFrame(3*np.random.rand(5),
#               index=['a','b','c','d','e'],columns=['x'])
# pf.plot.pie(subplots=True)
#
# import matplotlib.pyplot as plt
# name_list = ['Monday', 'Tuesday', 'Friday', 'Sunday']
# num_list = [1.5, 0.6, 7.8, 6]
# num_list1 = [1, 2, 3, 1]
# x = list(range(len(num_list)))
# total_width, n = 0.8, 2
# width = total_width / n
# plt.bar(x, num_list, width=width, label='boy', fc='y')
# for i in range(len(x)):
#     x[i] = x[i] + width
# plt.bar(x, num_list1, width=width, label='girl', tick_label=name_list, fc='r')
# plt.legend()
# plt.show()
# import numpy as np
# a = np.array([1,2,3],dtype=complex)
# print(a)





