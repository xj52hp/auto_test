# coding=utf-8
'''
Created on 2017-8-28
@author: lisq
Project:测试用例
'''
import unittest
from easyvaas.TestCase import TestCase as tc
#构造测试集
suite = unittest.TestSuite()
# suite.addTest(tc.TestCase('test_install'))
# suite.addTest(tc.TestCase('test_login'))
# suite.addTest(tc.TestCase('test_my'))
# suite.addTest(tc.TestCase('test_my_setting'))
# suite.addTest(tc.TestCase('test_my_share'))
# suite.addTest(tc.TestCase('test_home'))
# suite.addTest(tc.TestCase('test_create'))
suite.addTest(tc.TestCase('test_live'))

if __name__=='__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)