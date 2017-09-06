# -*- coding: utf-8 -*-

import unittest
import os
from appium import webdriver
from easyvaas.PO.deviceinfo import Getdeviceinfo as gd
from api.testDAL import appCase as ac

PATH = lambda p: os.path.abspath(
       os.path.join(os.path.dirname(__file__), p)
 )


class TestCase(unittest.TestCase):

    def test_login(self):
        print(PATH("../Case/login.yaml"))
        home_yaml = PATH("../Case/login.yaml")
        ac.AppCase.execCase(self, f=home_yaml)