# -*- coding: UTF-8 -*-
import os
import unittest
import time
import sys
from appium import webdriver

from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class LoginAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        #desired_caps['device'] = 'Z2X4C15804000415'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'm1 note'  # 这是测试机的型号，可以查看手机的关于本机选项获得
        desired_caps['appPackage'] = 'com.ccvideo'
        desired_caps['noReset'] = 'true'
        #desired_caps['appActivity']='com.yizhibo.video.activity.LoginMainActivity'
        #desired_caps['appActivity']='com.yizhibo.video.activity.HomeTabActivity'

        desired_caps['app'] = PATH('C:\\Users\\Administrator\\Desktop\\123.apk')
        #被测试的App在电脑上的位置

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()


    def myMethod(self,cid):
        print (cid)
        clogin = self.driver.find_element_by_id(cid)
        self.assertIsNotNone(clogin)
        clogin.click()
        return


    def test_login(self):
        time.sleep(5)
        # alogin = self.driver.find_element_by_id('com.ccvideo:id/dialog_continue_tv').click()

        blogin = self.driver.find_element_by_id('com.ccvideo:id/login_phone_iv').click()

        time.sleep(2)
        self.myMethod('com.ccvideo:id/add_option_tv')




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)





