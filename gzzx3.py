from selenium import webdriver
import requests
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
#from ddt import ddt,data,unpack
#import csv
from HTMLTestRunner import HTMLTestRunner
import os
import io

class TestDemo(unittest.TestCase):
      def setUp(self):
          self.driver = webdriver.Chrome()

      def test1_demo(self):
          self.driver.get('http://testmes.baozhuang.com/#/')
          time.sleep(2)
          self.driver.find_element_by_class_name('el-input__inner').send_keys('cym')
          self.driver.find_element_by_css_selector('#app > div > div > div > div > div > div.form-div > form > div:nth-child(2) > div > div.el-input.el-input--mini > input').send_keys('123456')
          self.driver.find_element_by_css_selector('#app > div > div > div > div > div > div.form-div > form > div:nth-child(3) > div > button').click()
          time.sleep(2)
          drop1_down=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/div/ul/li[2]/div/span')
          ActionChains(self.driver).click(drop1_down).perform()
          time.sleep(2)
          drop2_down=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/div/ul/li[2]/ul/li[8]/span')
          ActionChains(self.driver).click(drop2_down).perform()
          time.sleep(2)
          self.driver.find_element_by_css_selector('#app > div > div > div.container-box > div.router-box > div > div > div > div.right-table-part > div.right-btn-box > div > button:nth-child(1) > span').click()
          time.sleep(2)
          self.driver.find_element_by_class_name('el-input__inner').send_keys('cym01')
          time.sleep(2)
          self.driver.find_element_by_css_selector('#app > div > div > div.container-box > div.router-box > div > div > div > div.box-part > div > div > div.form-main.border-bottom > div > form > div:nth-child(1) > div:nth-child(2) > div > div.el-form-item__content > div > input').send_keys('cym预印机9色')
          time.sleep(2)
          self.driver.find_element_by_css_selector('#app > div > div > div.container-box > div.router-box > div > div > div > div.box-part > div > div > div.form-main.border-bottom > div > form > div:nth-child(1) > div:nth-child(3) > div > div.el-form-item__content > div > input').send_keys('cym预印机9色')
          #点击“类型”下拉框
          drop3_down=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div/div/div[1]/div/div/div[2]/div/form/div[1]/div[4]/div/div[2]/div/div/input')
          ActionChains(self.driver).click(drop3_down).perform()
          time.sleep(2)
          #设备
          self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[1]/span').click()
          time.sleep(2)
          #点击“是否有效”下拉框
          drop4_down=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div/div/div[1]/div/div/div[2]/div/form/div[1]/div[5]/div/div[2]/div/div/input')
          ActionChains(self.driver).click(drop4_down).perform()
          time.sleep(2)
          #是
          self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[1]').click()
          time.sleep(2)
          #点击“资源名称”下拉框
          drop5_down=self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div/div/div/div[1]/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div/input')
          ActionChains(self.driver).click(drop5_down).perform()
          time.sleep(2)
          #半自动圆模机MES测试
          self.driver.find_element_by_xpath("//span[text()=\"半自动圆模机MES测试\"]").click()
          # self.driver.find_element_by_css_selector('body > div:nth-child(9) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1) > span').click()
          time.sleep(2)
          self.driver.find_element_by_css_selector('#app > div > div > div.container-box > div.router-box > div > div > div > div.box-part > div > div > div.form-main.border-bottom > div > form > div:nth-child(2) > div.el-col.el-col-8 > div > div.el-form-item__content > div > input').send_keys('98-22-EF-F4-7B-B6')
          time.sleep(2)
          #保存
          self.driver.find_element_by_css_selector('#app > div > div > div.container-box > div.router-box > div > div > div > div.right-table-part > div.right-btn-box > div > button:nth-child(3) > span').click()
          time.sleep(2)
      def tearDown(self):
          self.driver.quit()
# if __name__ == '__main__':
#    unittest.main()

# def run():
#     testsuit = unittest.TestSuite()
#     testsuit.addTest(TestDemo("test1_demo"))
#     #定义测试报告存放路径
#     fp = open('result.html', 'wb')
#     #定义测试报告
#     runner = HTMLTestRunner(stream=fp, title='自动化测试报告',description='用例执行情况：')
#     runner.run(testsuit)
#     #关闭测试报告
#     fp.close()
#
# if __name__ == '__main__':
#    run()











