"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
import logging
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class LoginTests(unittest.TestCase):

    logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='testlogin.log',
                filemode='w')

    def setUp(self):
        # set up appium
        app = os.path.abspath('/Users/APPLE/Downloads/oupai.ipa')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '8.0.2',
                'deviceName': 'iPhone 5s'
            })

    def tearDown(self):
        self.driver.quit()

    # def _logininfoinput(self):
    #     # 调用进行手机号码和密码输入
    #     # 获取手机号码和密码控件
    #     phonenum = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextField[1]')
    #     password = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]')
    #     # 像两个控件中输入内容
    #     phonenum.send_keys('13784975654')
    #     # print(phonenum.text)
    #     password.send_keys('111111')
    #     # 验证输入内容是否相符
    #     self.assertEqual(phonenum.text, '13784975654')
    #     logging.info('phone number is right')
    #     # 后台获取密码的实际格式来对比，但是需验证是否有更好问题
    #     # self.assertEqual(password.text, '\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2')

    # def test_login(self):
    #     sleep(5)
    #     # 点击登录按钮
    #     self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[1]').click()
    #     self._logininfoinput()
            
    #     # 点击空白处将键盘隐藏
    #     self.driver.tap([(100, 100), ])
    #     # 点击忘记密码按钮
    #     self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[3]').click()

    #     sleep(5)
    # def test_yzb(self):
    #     # 首先睡几秒跳过广告页面
    #     sleep(5)
    #     # 睡几秒之后进入登录注册主页面


    def test_yzbmainframe(self):
        # 验证主界面元素
        # 首先睡几秒跳过广告页面
        sleep(5)
        # 睡几秒之后进入登录注册主页面
        # 验证logo元素图片
        logo = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAImage[1]')
        # 验证logo标签元素名称易直播
        logoname = self.driver.find_element_by_name('易直播')
        # 验证登录按钮
        loginbut = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[1]')
        # 验证注册按钮 
        registerbut = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[2]')
        # 验证第三方登录标签
        thirdparty = self.driver.find_element_by_name('第三方登录')
        # 验证第三方登录微博、微信、QQ按钮
        weibobut = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[3]')
        weixinbut = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[4]')
        qqbut = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[5]')
        logging.info('登录注册主界面没有问题')

        # 验证主界面点击事件
        # 点击注册按钮
        registerbut.click()
        self._createaccountframe()
        # 点击登录按钮
        # loginbut.click()
        # self._welcomeloginframe()

    def _createaccountframe(self):
        # 验证创建登录界面中的元素
        # 验证第一页导航栏
        loginfirst_page = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAImage[1]')
        # 验证创建账号标签
        createaccount = self.driver.find_element_by_name('创 建 账 号')
        # 验证时区按钮和默认的时区标签
        timezone = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[1]')
        defaulttimezone = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAStaticText[2]')
        # 验证手机号码输入栏
        phonenum = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextField[1]')
        # 验证获取验证码按钮
        testgetcodebut = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[2]')
        # 验证注册须知标签
        registration = self.driver.find_element_by_name('注册代表同意服务条款与隐私协议')
        # 验证服务条款和隐私协议链接
        servicetermslink = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAStaticText[3]/UIALink[1]')
        privacypolicylink = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAStaticText[3]/UIALink[2]')
        # 验证关闭按钮
        closebut = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[3]')
        logging.info("创建账号页面元素验证，没有问题")
        '''
        # 验证各个按钮的使用
        # 首先查看注册须知条款：服务条款和隐私协议
        servicetermslink.click()
        protocolcontent = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextView[1]')
        # 验证服务条款的文本
        if not "用户注册协议" in protocolcontent.text:
            raise TextError('服务条款文本错误')
        else:
            pass
        # 点击返回按钮
        backbut = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[1]')
        backbut.click()
        # 再同样验证一次隐私条款
        privacypolicylink.click()
        privacypolicybackbut = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[1]')
        privacypolicybackbut.click()
        logging.info("用户注册协议页面验证，没有问题")

        # 时区选择
        # 点击时区按钮进入时区选择页面
        timezone.click()
        # 验证返回上一级页面的响应区域
        returnfield = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]')
        # 验证国际区号列表标签
        listcodeslabel = self.driver.find_element_by_name('国际区号列表')
        # 验证国际区号的列表
        listcodes = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]')
        # 国际时区页面验证完成
        logging.info('国际时区列表页面验证，没问题')
        # 点击返回按钮的相应区域 
        returnfield.click()
        # 再次点击进入时区，点击一下埃及时区
        timezone.click()
        egyptzone = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[9]')
        egyptzone.click()
        # 验证更改后的默认时区不是+86，变味了+20
        self.assertEqual(defaulttimezone.text, '埃及 + 20')   
        # 再次点击进入时区，通过点击表格索引从新选择成+86
        timezone.click()
        self.driver.tap([(310, 493), ])
        chinazone = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[180]')
        chinazone.click()
        '''
        # 手机号码部分验证
        phonenum.send_keys('abc')
        

    def _welcomeloginframe(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
