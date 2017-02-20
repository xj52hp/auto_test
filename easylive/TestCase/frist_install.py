# -*- coding: utf-8 -*-

import os
import unittest
from appium import webdriver
from testDAL import appCase as ac
from TestCase import frist_login_phone as flp
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class testAPK_Install(unittest.TestCase):

    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '6.0.1',
        'deviceName': 'm1 note',
        'appPackage': 'com.ccvideo',
        'noReset': 'true',
        'app': 'C:\\Users\\Administrator\\Desktop\\123.apk'
    }

    def setUp(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)

    def test_install(self):

        home_login_yaml = PATH("E:\PycharmProjects\easylive\Case\Frist_apk_install.yaml")
        ac.AppCase.execCase(self, f=home_login_yaml)

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()
        pass



if __name__ == "__main__":
    unittest.main()
    flp.testFrist_Login.test_login()