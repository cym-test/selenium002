# coding=utf-8
import unittest
import HTMLTestRunner
#from utils.HTMLTestRunner-Python3 import HTMLTestRunner
import os
import io
from selenium002.gzzx3 import TestDemo

def suite():
    suite_test=unittest.TestSuite()
    suite_test.addTest(TestDemo("test1_demo"))
    #suite_test.addTest(Search("test2"))
    return suite_test

filePath='./result.html'
fp=open(filePath,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="测试报告",description="报告描述")

runner.run(suite())
fp.close()