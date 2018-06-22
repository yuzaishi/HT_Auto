# -*- coding:utf-8 -*-
__author__ = '朱永刚'
from selenium.webdriver.common.action_chains import ActionChains
from test.common.page import Page

class HTQicaoPage(Page):
    def page_qicao(self):
        # 基本信息
        self.driver.find_element_by_xpath('//*[@id="contractName"]').click()
        self.driver.find_element_by_xpath('//*[@id="contractName"]').send_keys('合同名称')  # 合同名称
        self.driver.find_element_by_xpath('/html/body/form/div/div[3]/fieldset/table/tbody/tr[3]/td[2]/select/option[2]').click()  # 收付款类别
        self.driver.find_element_by_xpath('//*[@id="xscontractSumMoney"]').send_keys('100000')  # 我方合同金额
        self.driver.find_element_by_id('contractBeginDate').send_keys('2018-06-30')  # 开始日期
        self.driver.find_element_by_id('contractOpteraterName').send_keys('我方经办人')  # 我方经办人
        self.driver.find_element_by_id('ownEntityPhone').send_keys('18666666666')  # 我方经办人电话
        self.driver.find_element_by_xpath('//*[@id="eventNo"]').send_keys('123456789')  # 项目号
        self.driver.find_element_by_id('contractEndDate').send_keys('2018-07-10')  # 结束日期
        self.driver.find_element_by_id('contractAssignPeople').send_keys('对方经办人')  # 对方经办人
        self.driver.find_element_by_id('otherEntityPhone').send_keys('15000000000')  # 对方经办人电话
        # 类别信息
        # self.driver.find_element_by_xpath('/html/body/form/div/div[4]/fieldset/table/tbody/tr[1]/td[2]/div[2]/label[1]/input').click()  # 所属级别--院级
        self.driver.find_element_by_xpath('/html/body/form/div/div[4]/fieldset/table/tbody/tr[1]/td[2]/div[2]/label[2]/input').click()  # 所属级别--所级
        self.driver.find_element_by_xpath('//*[@id="ext-gen15"]').click()  # ext属性，弹出框确认
        self.driver.find_element_by_xpath('//*[@id="conttype_input_name2c94e72e51131a700151134ee92a000c"]').click()
        menu2 = self.driver.find_element_by_xpath('//*[@id="2c94e72e5142c4c201514344a09a0005"]')  # 修改这个可以修改大类别
        ActionChains(self.driver).move_to_element(menu2).perform()
        self.driver.find_element_by_xpath('//*[@id="2c94e72e5142c4c201514350cd72000f"]').click()  # 合同类别
        self.driver.find_element_by_xpath('/html/body/form/div/div[4]/fieldset/table/tbody/tr[3]/td[2]/label[2]/input').click()  # 新增市场
        self.driver.find_element_by_xpath('/html/body/form/div/div[4]/fieldset/table/tbody/tr[4]/td[2]/label[2]/input').click()  # 涉外合同
        self.driver.find_element_by_xpath('/html/body/form/div/div[4]/fieldset/table/tbody/tr[1]/td[4]/label[2]/input').click()  # 联合合同
        self.driver.find_element_by_xpath('/html/body/form/div/div[4]/fieldset/table/tbody/tr[2]/td[4]/div[1]/label[2]/input').click()  # 基建合同
        self.driver.find_element_by_xpath('//*[@id="menu_input_name2c94e72e51131a700151134f102b000d"]').click()
        menu3 = self.driver.find_element_by_xpath('//*[@id="2c94e72e510f744001510fa3e4720031"]')  # 修改这个可以修改大类别
        ActionChains(self.driver).move_to_element(menu3).perform()
        self.driver.find_element_by_xpath('//*[@id="2c94e73055b9c6090155ba1f2145001d"]').click()  # 所属市场
        self.driver.find_element_by_xpath('/html/body/form/div/div[4]/fieldset/table/tbody/tr[4]/td[4]/label[2]/input').click()  # 三重一大
        # 签署信息
        self.driver.find_element_by_xpath('//*[@id="ownEntityIdsjgs"]').click()
        self.driver.find_element_by_xpath('/html/body/form/div/div[5]/fieldset/table/tbody/tr[1]/td[2]/select[2]/option[2]').click()  # 所级合同我方实体
        '''
        self.driver.find_element_by_xpath('//*[@id="ownEntityIdyj"]').click()
        self.driver.find_element_by_xpath('/html/body/form/div/div[5]/fieldset/table/tbody/tr[1]/td[2]/select[1]/option[2]').click()# 院级合同我方实体
        '''
        self.driver.find_element_by_xpath('//*[@id="otherEntityName"]').send_keys('')  # 对方实体
        self.driver.find_element_by_xpath('//*[@id="ownAssignPeople"]').send_keys('魏青')  # 我方签订人
        self.driver.find_element_by_xpath('//*[@id="otherOpteraterName"]').send_keys('梵高')  # 对方签订人
        # 合同文本及相关证明文件
        self.driver.find_element_by_xpath('//*[@id="ourHTFile0"]').send_keys(r'E:\测试项目汇总\11-合同管理系统\sc上传附件\第四方合同签订依据.doc')  # 上传附件
        # 收付款计划
        self.driver.find_element_by_xpath('//*[@id="xsplanMoney0"]').click()
        self.driver.find_element_by_xpath('//*[@id="xsplanMoney0"]').send_keys('100000')  # 第一笔金额
        # js = "document.getElementById('txtBeginDate').removeAttribute('readonly')"  # 1.原生js，移除属性
        # js = "$('input[id=txtBeginDate]').removeAttr('readonly')"  # 2.jQuery，移除属性
        js = "$('input[id=LHHT1_1SJ]').attr('readonly',false)"  # 3.jQuery，设置为false
        # js = "$('input[id=txtBeginDate]').attr('readonly','')"  # 4.jQuery，设置为空（同3）
        self.driver.execute_script(js)
        self.driver.find_element_by_xpath('//*[@id="LHHT1_1SJ"]').send_keys('2018-06-30')  # 第一笔金额时间
        self.driver.find_element_by_xpath('/html/body/form/div/div[7]/fieldset/table[2]/tbody/tr/td/div/table/tbody/tr/td[6]/input').send_keys('收付款计划备注')
        # 备注
        # self.driver.find_element_by_xpath('//*[@id="description"]').send_keys('合同描述')
        self.driver.find_element_by_xpath('//*[@id="remark"]').send_keys('备注')
        self.driver.find_element_by_xpath('//*[@id="save_btn"]').click()
        self.driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]').click()
