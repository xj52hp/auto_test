# coding=utf-8
'''
Created on 2017-9-02
@author: lisq
Project:测试用例
'''
import unittest
from api.TestCase import TestCase as tc
#构造测试集
suite = unittest.TestSuite()
suite.addTest(tc.TestCase('test_login'))

if __name__=='__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)