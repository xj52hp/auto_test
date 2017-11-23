import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
def GetCookie():
    url = "http://you.autohome.com.cn/"
    Chrome = webdriver.Chrome()
    Chrome.get(url)
    Chrome.maximize_window()
    #点击首页轮播图
    Chrome.find_element_by_id("big-img").click()
    #新页中断言页面属性
    time.sleep(3)

    EC.title_contains("游记详情")
    Chrome.find_elements_by_class_name("num fl")

    # aa = Chrome.find_element_by_tag_name('h4').value_of_css_property('em')
    # print(aa)
    # if Chrome.find_elements_by_class_name("img-responsive user-pic"):








    Chrome.close()



    # aa = Chrome.window_handles
    # print(aa)


    time.sleep(10)



    #
    #
    #
    # url = "http://you.autohome.com.cn/"
    # cookies = []
    # try:
    #     print('open IE browser')
    #     ie = webdriver.Chrome()
    #     print('visit cnvd website')
    #     ie.get(url)
    #     timesleep = 8 #需要延时，来获取完整的cookies
    #     print('sleep {} seconds'.format(timesleep))
    #     time.sleep(timesleep) # important to get full cookies
    # except WebDriverException as wde:
    #     print(wde)
    #     if ie != None:
    #         ie.quit()
    # else:
    #     print('get cookies...')
    #     cookies = ie.get_cookies()
    #     ie.quit()
    #
    # if cookies == '' or type(cookies) != list  or cookies.__len__() == 0:
    #     print('cookie is not found')
    # else:
    #     print('cookies: {}, size: {}'.format(cookies, cookies.__len__()))
    #


GetCookie()