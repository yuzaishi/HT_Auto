# -*- coding:utf-8 -*-
__author__ = '朱永刚'
from selenium.webdriver.common.action_chains import ActionChains
from test.common.page import Page
from selenium.webdriver.common.by import By

class HTOpenPage(Page):
    """
    打开最上边一排菜单，hover为悬停的元素，click为最终点击的元素，所有元素保存在yuansudingwei.xlsx的Sheet4下
    """
    def page_openPage(self,hover,click):
        self.driver.switch_to_frame('topFrame')
        menu = self.driver.find_element_by_xpath(hover)
        ActionChains(self.driver).move_to_element(menu).perform()
        self.driver.find_element_by_xpath(click).click()
