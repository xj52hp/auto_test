#coding=utf-8  

import os 

from selenium import webdriver 

PATH = lambda p: os.path.abspath(  

 

os.path.join(os.path.dirname(__file__), p) 

) 

 

desired_caps = {} 

desired_caps['platformName'] = 'Android' 

 

 

desired_caps['version'] = '4.4.2' 

desired_caps['deviceName'] = 'emulator-5554' 

desired_caps['appPackage'] = 'com.android.calculator2' 

desired_caps['appActivity'] = '.Calculator' 
 

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
 

driver.find_element_by_id("com.android.calculator2:id/digit1").click() 

driver.find_element_by_id("com.android.calculator2:id/plus").click() 

driver.find_element_by_id("com.android.calculator2:id/digit2").click() 

driver.find_element_by_id("com.android.calculator2:id/equal").click() 

 

driver.quit() 


