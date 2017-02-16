# -*- coding: utf-8 -*-
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
from PO import BasePage
import time
'''
手机登录封装
'''

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', BasePage.Base.capabilities)

class Dash(BasePage.Base):
    login_phone_loc = (By.ID,"com.ccvideo:id/login_phone_iv")
    country_loc = (By.ID,"com.ccvideo:id/select_country_tv")
    phone_loc = (By.ID,"com.ccvideo:id/register_phone_et")
    pwd_loc = (By.ID,"com.ccvideo:id/password_et")
    def click_phone_login(self):
        self.find_element(self.login_phone_loc)

    def check_country(self):
        self.find_element(self.country_loc).click()
    def click_phone(self):
        self.find_element(self.phone_loc).click()

    def click_pwd(self):
        self.find_element(self.pwd_loc).click()
    def input_phone(self,phone_recipe):
        self.send_keys(self.phone_loc,phone_recipe)
    def input_pwd(self,pwd_recipe):
        self.send_keys(self.pwd_loc,pwd_recipe)

def login(phone_recipe,pwd_recipe):
    dash_page = Dash(driver)
    print(phone_recipe,pwd_recipe)
    time.sleep(4)
    dash_page.click_phone_login()
    print('电话号码：') + phone_recipe
    dash_page.input_phone(phone_recipe)
    dash_page.click_pwd()
    print('密码：') + pwd_recipe
    dash_page.input_phone(pwd_recipe)

    driver.quit()

