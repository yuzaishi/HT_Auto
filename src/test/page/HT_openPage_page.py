# -*- coding:utf-8 -*-
__author__ = '朱永刚'
from selenium.webdriver.common.action_chains import ActionChains
from test.common.page import Page
from time import sleep

class HTOpenPage(Page):
    def page_openPage(self):
        self.driver.switch_to_frame('topFrame')
        menu = self.driver.find_element_by_xpath('/html/body/div[3]/ul/li[3]/h3/a/div/span')
        ActionChains(self.driver).move_to_element(menu).perform()
        self.driver.find_element_by_xpath('/html/body/div[3]/ul/li[3]/ul/li[1]/h3/a').click()
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame('mainFrame')
        sleep(0.5)  # 如果无法跳转到起草页面，将等待时间调大，经测试最小可以调到0.3
