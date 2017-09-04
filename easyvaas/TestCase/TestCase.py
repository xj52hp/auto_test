# -*- coding: utf-8 -*-

import unittest
import os
from appium import webdriver
from easyvaas.PO.deviceinfo import Getdeviceinfo as gd
from easyvaas.testDAL import appCase as ac

PATH = lambda p: os.path.abspath(
       os.path.join(os.path.dirname(__file__), p)
 )


class TestCase(unittest.TestCase):

    def setUp(self):
        self.desired_caps = gd.get_deviceinfo(self)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)

    def tearDown(self):
        self.driver.quit() #case执行完退出

    def test_install(self):
        home_yaml = PATH("../Case/install.yaml")
        ac.AppCase.execCase(self, f=home_yaml)

    def test_login(self):
        home_yaml = PATH("../Case/login.yaml")
        ac.AppCase.execCase(self, f=home_yaml)

    def test_my(self):
        home_yaml = PATH("../Case/my.yaml")
        ac.AppCase.execCase(self, f=home_yaml)
    def test_my_setting(self):
        home_yaml = PATH("../Case/my_setting.yaml")
        ac.AppCase.execCase(self, f=home_yaml)
    def test_my_share(self):
        home_yaml = PATH("../Case/my_share.yaml")
        ac.AppCase.execCase(self, f=home_yaml)
    def test_my_home(self):
        home_yaml = PATH("../Case/home.yaml")
        ac.AppCase.execCase(self, f=home_yaml)
    def test_create(self):
        home_yaml = PATH("../Case/create.yaml")
        ac.AppCase.execCase(self, f=home_yaml)
    def test_live_setting(self):
        home_yaml = PATH("../Case/live_setting.yaml")
        ac.AppCase.execCase(self, f=home_yaml)
    def test_live_detail(self):
        home_yaml = PATH("../Case/live_detail.yaml")
        ac.AppCase.execCase(self, f=home_yaml)

if __name__ == "__main__":
    unittest.main()