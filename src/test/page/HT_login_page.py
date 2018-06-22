# -*- coding:utf-8 -*-
__author__ = '朱永刚'
from test.common.page import Page

class HTLoginPage(Page):
    def page_login(self,loginName,passwd=111111):
        self.loginName = loginName
        self.passwd = passwd
        self.driver.find_element_by_xpath('/html/body/div[3]/form/div/div/div/div[1]/input').send_keys(loginName)
        self.driver.find_element_by_xpath('/html/body/div[3]/form/div/div/div/div[2]/input').send_keys(passwd)
        self.driver.find_element_by_xpath('/html/body/div[3]/form/div/div/div/div[3]/input').click()