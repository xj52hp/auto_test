#!/usr/bin/python
#encoding:utf-8
#test.py

import re
import sys
import os
import string
import locale
import java
import time

from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
from com.android.monkeyrunner.easy import EasyMonkeyDevice  as ed
from com.android.monkeyrunner.easy import By
from com.android.chimpchat.hierarchyviewer import HierarchyViewer as hv
#from com.android.hierarchyviewer2lib.device import ViewNode 
#from com.dtmilano.android.viewclient import ViewClient
#from com.dtmilano.android.wrapEasyMonkey import wrapEasyMonkey



print('连接设备')
device = mr.waitForConnection()
if device: 
    print('设备连接成功\n')      
else: 
    print >> mr.sys.stderr,"fail"  
    mr.sys.exit(1) 
print('连接设备成功')          



# print('##########################################安装包############################################')
# device.removePackage('com.changyou.mgp.sdk.mbi')
# print('卸载成功\n')
# install = device.installPackage("D:\\work\\Cyou\\SDK\\Android-CY\\1.08.050-R\\CYMG-0317-1.08.050-CY.apk")
# if (install <> ''):
#     a='安装成功\n'
#     print(a)
# print('##########################################安装包成功############################################')


            
print('启动Activity')  
start = device.startActivity("com.changyou.mgp.sdk.mbi/com.changyou.mgp.sdk.mbi.test.activity.SDKScreenChoiceActivity")
# device.startActivity(component="com.changyou.mgp.sdk.mbi/com.changyou.mgp.sdk.mbi.test.activity.SDKLauncherActivity")
if (start <> ''):
    print('启动成功\n')
mr.sleep(3)
mydevice = ed(device)
print('启动Activity完成')  
 
# will getHierarchyViewer();
# 初始化&登录
mr.sleep(2)
mydevice.touch(By.id('id/sdk_release_rb'),md.DOWN_AND_UP)
mydevice.touch(By.id('id/sdk_portrait_btn'),md.DOWN_AND_UP)
mr.sleep(5)
 
         
#点击登录按钮
print('初始化成功\n')
mydevice.touch(By.id('id/sdk_login_btn'),md.DOWN_AND_UP)
viewer = mydevice.getHierarchyViewer()
mr.sleep(3)
login_btn_oneKeyRegister = viewer.findViewById('id/login_btn_oneKeyRegister')
         
try:    
    viewer.getText(login_btn_oneKeyRegister).encode('utf-8') == '一秒注册'
    a = 1
except :
    a = 2
  
if (a == 1):
    mr.sleep(5)# 登录页面测试#一秒注册     
    mydevice.touch(By.id('id/login_btn_oneKeyRegister'),md.DOWN_AND_UP)
    mr.sleep(5)
    quick_into_account_et = viewer.findViewById('id/quick_into_account_et')
    text = viewer.getText(quick_into_account_et).encode('utf-8')
    if (text == ''):
        print("用户名空，手动输入\n")
        mydevice.type(By.id('id/quick_into_account_et'),'lsq098121')
    mydevice.type(By.id('id/quick_into_password_et'),"woshixiao9")         
    button = viewer.findViewById('id/quick_into_btn_know')
    mydevice.touch(By.id('id/quick_into_btn_know'),md.DOWN_AND_UP)
    text = viewer.getText(button).encode('utf-8')
    print('点击'+text+'成功')
    mr.sleep(5)
    sdk_get_goodslist_btn = viewer.findViewById('id/sdk_get_goodslist_btn')
    text = viewer.getText(sdk_get_goodslist_btn).encode('utf-8')
    if (text == '获取商品列表'):
        print("登录成功\n")
        print("获取商品列表成功\n")
       
    
else :
    mr.sleep(3)
    sdk_get_goodslist_btn = viewer.findViewById('id/sdk_get_goodslist_btn')
    text = viewer.getText(sdk_get_goodslist_btn).encode('utf-8')
    if (text == "获取商品列表"):
        print("自动登录成功\n")
        print("获取商品列表成功\n")
    else:
        print("自动登录失败\n")
          
 
#注销与自动登录
print('注销与老帐号登录功能测试\n')
mr.sleep(3)
sdk_get_goodslist_btn = viewer.findViewById('id/sdk_get_goodslist_btn')
text = viewer.getText(sdk_get_goodslist_btn).encode('utf-8')
# text = '获取商品列表'
if (text == "获取商品列表"):
    print("获取商品列表成功\n")
    sdk_loginout_btn = viewer.findViewById('id/sdk_loginout_btn')
    text = viewer.getText(sdk_loginout_btn).encode('utf-8')
#     text = '注销'
    if (text == "注销"):
        mydevice.touch(By.id('id/sdk_loginout_btn'),md.DOWN_AND_UP)
        mr.sleep(1)
        print("注销成功\n")
        mydevice.touch(By.id('id/sdk_login_btn'),md.DOWN_AND_UP)
        mr.sleep(5)
        print('输入用户名&密码')
        viewer = mydevice.getHierarchyViewer()
        login_et_account = viewer.findViewById('id/login_et_account')
        text = viewer.getText(login_et_account).encode('utf-8')  
#         print(text) 
        if (text <> ''):
            mydevice.touch(By.id('id/login_et_account'),md.DOWN)
            mr.sleep(3)
            print('清空帐号内容，输入老帐号信息进行登录测试\n')
            mydevice.press('KEYCODE_DEL','DOWN_AND_UP')
        else:
            print('老帐号清理失败，测试不通过')
        mydevice.type(By.id('id/login_et_account'),"18911373631")
        mydevice.type(By.id('id/login_et_password'),"woshixiao10")
        mydevice.touch(By.id('id/login_btn_login'),md.DOWN_AND_UP)
        mr.sleep(5)
        sdk_get_goodslist_btn = viewer.findViewById('id/sdk_get_goodslist_btn')
        text = viewer.getText(sdk_get_goodslist_btn).encode('utf-8')
        if (text == "获取商品列表"):
            print("登录成功\n")
            print("获取商品列表成功\n")
        else:
            mr.sleep(5)
            print("登录失败\n")        
else:
    print('未在登录界面，注销再登录功能未执行成功')
  
  
  
  
#悬浮窗显示与隐藏
print('悬浮窗显示与隐藏的测试')
mr.sleep(3)
sdk_get_goodslist_btn = viewer.findViewById('id/sdk_get_goodslist_btn')
text = viewer.getText(sdk_get_goodslist_btn).encode('utf-8')
if (text == "获取商品列表"):
    print("获取商品列表成功\n")
    pic_hide_1=device.takeSnapshot()
    mydevice.touch(By.id('id/sdk_show_float_btn'),md.DOWN_AND_UP)
    mr.sleep(7)
    pic_show_1=device.takeSnapshot()
    mydevice.touch(By.id('id/sdk_hide_float_btn'),md.DOWN_AND_UP)
    pic_hide_2=device.takeSnapshot()
    mydevice.touch(By.id('id/sdk_show_float_btn'),md.DOWN_AND_UP)
    pic_show_2=device.takeSnapshot()
     
    if pic_hide_2.sameAs(pic_hide_1,1.0) :
        print ('隐藏悬浮窗按钮对比OK')
    else:
        print ('隐藏悬浮窗按钮对比错误')
    if pic_show_2.sameAs(pic_show_1,1.0) :
        print ('显示悬浮窗按钮对比OK')
    else:
        print ('显示悬浮窗按钮对比错误')
 
      
else:
    print('未执行悬浮框显示功能')



      
        
        
#返回主界面，重新启动应用，切换帐号
print('返回主界面，重新启动应用，切换帐号')
mydevice.press('KEYCODE_BACK','DOWN_AND_UP')
mr.sleep(3)
print('重新启动Activity')  
start = device.startActivity("com.changyou.mgp.sdk.mbi/com.changyou.mgp.sdk.mbi.test.activity.SDKScreenChoiceActivity")
if (start <> ''):
    print('启动成功\n')
mr.sleep(3)
print('Activity完成')  
 
# will getHierarchyViewer();
# 初始化&登录
mr.sleep(2)
mydevice.touch(By.id('id/sdk_release_rb'),md.DOWN_AND_UP)
mydevice.touch(By.id('id/sdk_portrait_btn'),md.DOWN_AND_UP)
print('初始化成功\n')
mr.sleep(5)
mydevice.touch(By.id('id/sdk_login_btn'),md.DOWN_AND_UP)


mydevice.touch(By.id('id/mgp_auto_login_switch_acc_tv'),md.DOWN_AND_UP)
mydevice.touch(By.id('id/mgp_auto_login_switch_acc_tv'),md.DOWN_AND_UP)
mydevice.touch(By.id('id/mgp_auto_login_switch_acc_tv'),md.DOWN_AND_UP)
mydevice.touch(By.id('id/mgp_auto_login_switch_acc_tv'),md.DOWN_AND_UP)


try:
    mydevice.touch(By.id('id/mgp_auto_login_switch_acc_tv'),md.DOWN_AND_UP)
    print('切换帐号按钮点击成功，无需尝试坐标切换')
    b = 1
except:
    print('切换帐号失败，尝试坐标切换')
    b = 2
if b == 2 :
    
    #返回主界面，重新启动应用，切换帐号
    print('返回主界面，重新启动应用，切换帐号')
    mr.sleep(5)
    mydevice.press('KEYCODE_BACK','DOWN_AND_UP')
    mr.sleep(3)
    print('重新启动Activity')  
    start = device.startActivity("com.changyou.mgp.sdk.mbi/com.changyou.mgp.sdk.mbi.test.activity.SDKScreenChoiceActivity")
    if (start <> ''):
        print('Activity启动完成')  
        # 初始化&登录
        mr.sleep(5)
        mydevice.touch(By.id('id/sdk_release_rb'),md.DOWN_AND_UP)
        mydevice.touch(By.id('id/sdk_portrait_btn'),md.DOWN_AND_UP)
        print('初始化成功\n')
        mr.sleep(5)
        mydevice.touch(By.id('id/sdk_login_btn'),md.DOWN_AND_UP)
        q = device.touch(280,312,'DOWN_AND_UP')
        mydevice.touch(280,380,'DOWN_AND_UP')
        mydevice.touch(280,390,'DOWN_AND_UP')
        mydevice.touch(280,400,'DOWN_AND_UP')
        if q:
            print('点击。。。。。。。。。。')
        mr.sleep(3)
        try:    
            viewer.getText(login_btn_oneKeyRegister).encode('utf-8') == '一秒注册'
            aa = 1
        except :
            print('切换帐号失败\n')
        if aa == 1:
            print('切换帐号成功\n')
            print('输入用户名&密码')
            mydevice.type(By.id('id/login_et_account'),"15810627114")
            mydevice.type(By.id('id/login_et_password'),"woshixiao9")
            mydevice.touch(By.id('id/login_btn_login'),md.DOWN_AND_UP)
            mr.sleep(5)
            sdk_get_goodslist_btn = viewer.findViewById('id/sdk_get_goodslist_btn')
            text = viewer.getText(sdk_get_goodslist_btn).encode('utf-8')
            if (text == "获取商品列表"):
                print("登录成功\n")
            else:
                print("登录失败\n")
            print('切换帐号完成')
    else:
        print('启动失败\n')

else:
    print('切换帐号按钮点击成功')   
    print('点击切换帐号按钮')
    print('输入用户名&密码')        
    mydevice.type(By.id('id/login_et_account'),"15810627114")
    mydevice.type(By.id('id/login_et_password'),"woshixiao9")
    mydevice.touch(By.id('id/login_btn_login'),md.DOWN_AND_UP)
    mr.sleep(5)
    sdk_get_goodslist_btn = viewer.findViewById('id/sdk_get_goodslist_btn')
    text = viewer.getText(sdk_get_goodslist_btn).encode('utf-8')
    if (text == "获取商品列表"):
        print("登录成功\n")
    else:
        mr.sleep(5)
        print("登录失败\n")    
    
    
print ('test finished!')
         
    
