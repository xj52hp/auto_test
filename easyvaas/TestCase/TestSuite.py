# coding=utf-8
'''
Created on 2017-8-28
@author: lisq
Project:测试用例
'''
import unittest
from easyvaas.TestCase import TestCase as tc
import os
import time
from easyvaas.PO import HTMLTestRunner
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
result = "../report/"

#构造测试集
suite = unittest.TestSuite()
suite.addTest(tc.TestCase('test_install'))
suite.addTest(tc.TestCase('test_login'))
suite.addTest(tc.TestCase('test_my'))
suite.addTest(tc.TestCase('test_my_setting'))
suite.addTest(tc.TestCase('test_my_share'))
suite.addTest(tc.TestCase('test_my_home'))
suite.addTest(tc.TestCase('test_create'))
suite.addTest(tc.TestCase('test_live_setting'))
suite.addTest(tc.TestCase('test_live_detail'))

if __name__=='__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    # runner.run(suite)

    #获取系统当前时间
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    #定义单个测试报告的存放路径，支持相对路径
    tdresult = result + day

    #若已经存在以当天日期为名称的文件夹的情况，则直接将测试报告放到这个文件夹之下
    if os.path.exists(tdresult) is not True:
        #不存在以当天日期为名称的文件夹的情况，则建立一个以当天日期为名称的文件夹
        os.mkdir(tdresult)
    #以写文本文件或写二进制文件的模式打开测试报告文件
    filename = tdresult + '/' + now + "_result.html"
    fp = open(filename, 'wb')
    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='自动化测试报告', description='用例执行情况：')
    #运行测试用例
    runner.run(suite)
    #关闭报告文件
    fp.close()