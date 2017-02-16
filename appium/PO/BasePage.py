# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
import time,os
import unittest
from appium import webdriver

class Base:
    #driver = None
    capabilities = {'platformName':'Android',
                        'platformVersion':'6.0.1',
                        'deviceName':'m1 note',
                        'appPackage':'com.ccvideo',
                        'noReset':'True',
                        'app':'C:\\Users\\Administrator\\Desktop\\123.apk'
                    }
    def __init__(self,appium_driver):
        self.driver = appium_driver
    def find_element(self,loc):
        try:
            WebDriverWait(self.driver,15).until(lambda driver:driver.find_element)
            return self.driver.find_element(*loc)
        except:
            print ('%s 页面中为能找到 %s 元素' %(self,loc))