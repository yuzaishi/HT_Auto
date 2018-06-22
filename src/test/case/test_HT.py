# -*- coding:utf-8 -*-
__author__ = '朱永刚'
import os
import time
import unittest
from utils.config import Config,DRIVER_PATH,DATA_PATH,REPORT_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.mail import Email
from test.page.HT_login_page import HTLoginPage
from test.page.HT_openPage_page import HTOpenPage
from test.page.HT_qicao_page import HTQicaoPage
from selenium.webdriver.common.action_chains import ActionChains

class TestHeTong(unittest.TestCase):
    URL = Config().get('URL')
    EXCLE = os.path.join(DATA_PATH,'hetong.xlsx')

    def sub_setUp(self):
        self.page = HTLoginPage(browser_type='firefox').get(self.URL,maxmize_windows=False)

    def sub_tearDown(self):
        self.page.quit()

    def test_qicao(self):
        datas = ExcelReader(self.EXCLE).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.page_login(d['loginName']) # 登录
                HTOpenPage.page_openPage(self.page) # 打开起草界面
                HTQicaoPage.page_qicao(self.page) # 填写起草信息

if __name__ == '__main__':#Alt + Shift +F10 以文件模式执行会出报告
    #unittest.main()
    # 报告格式
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report = REPORT_PATH + r'\\' + now + 'report.html'
    f = open(report, 'wb')
    runner = HTMLTestRunner(f, verbosity=2, title=u'合同测试报告', description=u'用例执行情况')
    runner.run(TestHeTong('test_qicao'))
    Email(file_path=report).send()#发送邮件

