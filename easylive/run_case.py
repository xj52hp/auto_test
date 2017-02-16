# -*- coding: utf-8 -*-
from appium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time,os
import unittest
from PO import OperateElement
import HTMLTestRunner


case_path = ".\\TestCase"
result = ".\\Result\\"


def Creatsuite():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path,pattern='Test_*.py',top_level_dir=None)


    for test_suite in discover:
        for casename in test_suite:
            testunit.addTest(casename)
        print(testunit)
    return testunit

test_case = Creatsuite()


now = time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))
day = time.strftime('%Y-%m-%d',time.localtime(time.time()))

tdresult = result + day

if os.path.exists(tdresult):
    filename = tdresult + "\\" + now + "_result.html"
    fp = file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'APPium测试报告',description=u'用例详情：')
    runner.run(test_case)
    fp.close()