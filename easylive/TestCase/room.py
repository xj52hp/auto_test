# -*- coding: utf-8 -*-

import os
import unittest
from appium import webdriver
from easylive.testDAL import appCase as ac

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class testroom(unittest.TestCase):

    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '6.0',
        'deviceName': 'm1 note',
        'appPackage': 'com.ccvideo',
        'noReset': 'true',
        # 'automationName': 'Selendroid',
        'app': '/work/123.apk'
    }
    def setUp(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)

    def test_search(self):

        home_login_yaml = PATH("/work/Pycharm_Product/auto_test/easylive/Case/Room.yaml")
        ac.AppCase.execCase(self, f=home_login_yaml)



    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()
        pass



if __name__ == "__main__":
    unittest.main()
