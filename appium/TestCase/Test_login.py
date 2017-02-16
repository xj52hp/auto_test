# -*- coding: utf-8 -*-

import unittest
from appium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from PO import DashPage,BasePage

class Login(unittest.TestCase):

    def setUp(self):
        phone_recipe_list = ['18911373631','18811742364']
        self.phone_recipe = phone_recipe_list[-1]
        pwd_recipe_list = ['222222','111111']
        self.pwd_recipe = pwd_recipe_list[-1]

    def test_Login(self):

        DashPage.login(self.phone_recipe,self.pwd_recipe)


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
