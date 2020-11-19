import os
import time
import  unittest
from yj_application_apiTest.config import pathconfig
from yj_application_apiTest.tools import htmlTestRunner
from yj_application_apiTest.tools.filePath import fileposition
from yj_application_apiTest.tools.sendEmailTools import sendEmai
# 报告存放地址 ====在配置文件配置
reportdir=pathconfig.reportdir
# 用例存放地址====在配置文件配置
casedir=pathconfig.casedir

def runall_case():
    discover = unittest.defaultTestLoader.discover(casedir, pattern='test_*.py',top_level_dir=None)
    testcase=unittest.TestSuite()
    for test_suit in discover:
        for test_case in test_suit:
            testcase.addTests(test_case)
    # testcase.addTests(discover)
    return  testcase
if __name__=="__main__":
    # runner=unittest.TextTestRunner()
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # 2、html报告文件路径
    report_abspath = os.path.join(reportdir, "result_" + now + ".html")
    # 3、打开一个文件，将result写入此file中
    fp = open(report_abspath, "wb")
    runner = htmlTestRunner.HTMLTestRunner(stream=fp,title=u'接口自动化测试报告,测试结果如下：',description=u'用例执行情况：')
    runner.run(runall_case())
    fp.close()
    # 发送结果到邮箱
    newresult = fileposition.new_file(reportdir)
    emial = sendEmai
    emial.Sendemail(newresult)