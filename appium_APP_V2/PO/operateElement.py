# -*- coding: utf-8 -*-
from assertpy import assert_that
from appium_APP_V2.PO.variable import GetVariable as common
from appium_APP_V2.PO import operateYaml as gt
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium.common.exceptions
import time,re,os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
temp_file = "../Case/Casetemp.txt"

class OperateElement():
    def __init__(self, driver=""):
        self.driver = driver

    def findElement(self, mOperate):
        try:
            WebDriverWait(self.driver, common.WAIT_TIME).until(lambda x: elements_by(mOperate, self.driver))
            return True
        except selenium.common.exceptions.TimeoutException:
            return False
        except selenium.common.exceptions.NoSuchElementException:
            return False
        except:
            return False
    def operate_element(self, mOperate):
        if OperateElement.findElement(self, mOperate):
            elements = {
                common.CLICK: lambda: operate_click(mOperate, self.driver),
                common.SEND_KEYS: lambda: send_keys(mOperate, self.driver),
                common.ATTRIBUTES: lambda: operate_attributes(mOperate, self.driver),
                common.SWIPELEFT: lambda: opreate_swipe_left(self, mOperate),
                common.SWIPEDOWN: lambda: opreate_swipe_down(self, mOperate),
                common.SWIPEUP: lambda: opreate_swipe_up(self, mOperate),
                common.SWIPERIGHT: lambda: opreate_swipe_right(self, mOperate),
                common.FIND_STR: lambda: find_str(mOperate, self.driver),
                common.FIND_STRS: lambda: find_strs(mOperate, self.driver),
                common.SAVE_STRS: lambda: save_strs(mOperate, self.driver),
                common.DIFF_NUM: lambda: diff_num(mOperate, self.driver),
                common.DIFF_STRS: lambda: diff_strs(mOperate, self.driver),
                common.SYSTEM_BUTTON: lambda: system_button(mOperate, self.driver),
                common.COMMENT_REGION: lambda: comment_region(mOperate, self.driver),
                common.NOW_DAY: lambda: getNowday(mOperate, self.driver),
                common.FIND_TOAST: lambda: find_toast(mOperate, self.driver)
            }
            return elements[mOperate["operate_type"]]()
        return False

# 封装常用的标签
def elements_by(mOperate, cts):
    elements = {
        common.find_element_by_id: lambda: cts.find_element_by_id(mOperate["element_info"]),
        common.find_elements_by_id: lambda: cts.find_elements_by_id(mOperate["element_info"]),
        common.find_element_by_xpath: lambda: cts.find_element_by_xpath(mOperate["element_info"]),
        common.find_element_by_name: lambda: cts.find_element_by_name(mOperate['name']),
        common.find_elements_by_name: lambda: cts.find_elements_by_name(mOperate['name'])[mOperate['index']],
        common.find_element_by_class_name: lambda: cts.find_element_by_class_name(mOperate['element_info']),
        common.find_elements_by_class_name: lambda: cts.find_elements_by_class_name(mOperate['element_info'])[
            mOperate['index']]
    }
    return elements[mOperate["find_type"]]()


#--------封装事件与业务----------#


# 点击事件
def operate_click(mOperate, cts):
    if mOperate["find_type"] == common.find_element_by_id or mOperate["find_type"] == common.find_element_by_name or mOperate["find_type"] == common.find_element_by_xpath:
        elements_by(mOperate, cts).click()
    if mOperate["find_type"] == common.find_elements_by_id or mOperate["find_type"] == common.find_elements_by_name:
        elements_by(mOperate, cts)[mOperate["index"]].click()
    if common.SELENIUM_APPIUM == common.APPIUM:
        pass
#断言控件属性
def operate_attributes(mOperate, cts):
    try:
        va = elements_by(mOperate, cts).get_attribute(mOperate['attributes_key'])
        print("预期:          ", str.lower(mOperate['text']))
        assert_that(str.lower(va)[0:1]).is_equal_to(str.lower(mOperate['text']))
        return True
    except AssertionError as e:
        print("实际:          不相同或者元素的属性不正确:", e)
        return False
#发送文字
def send_keys(mOperate, cts):
    try:
        elements_by(mOperate, cts).set_text(mOperate['text'])
        print('预期:          ', mOperate['text'])
        return True
    except:
        print('实际:          输入错误')
        return False
#断言字符串相等
def find_str(mOperate, cts):
    find_string = elements_by(mOperate, cts).text
    try:
        assert_that(str(find_string)).is_equal_to(str(mOperate['text']))
        print('预期:          ', find_string)
        return True
    except AssertionError as e:
        print("预期:          相同: ", e)
        return False
#断言字符串包含
def find_strs(mOperate, cts):
    find_strings = elements_by(mOperate, cts).text
    try:
        assert_that(str(mOperate['text'])).is_subset_of(str(find_strings))
        print('预期:          ', find_strings)
        return True
    except AssertionError as e:
        print("预期:          包含: ", e)
        return False
#保存字符串到临时文件
def save_strs(mOperate, cts):
    bo = gt.writeTxt(temp_file, elements_by(mOperate, cts).text)
    print('预期:          ', elements_by(mOperate, cts).text)
    return bo
#对比数字
def diff_num(mOperate, cts):
        time.sleep(3)
        x = gt.getTxt(temp_file)
        x = re.sub("\D", "", x)
        y = re.sub("\D", "", elements_by(mOperate, cts).text)
        if mOperate['operate_name'] == "roll":
            y = re.sub("\D", "", x)
            x = re.sub("\D", "", elements_by(mOperate, cts).text)

        if int(x) == int(y) + int(mOperate['cost_num']):
            print('预期:          变化: ', int(mOperate['cost_num']))
            return True
        else:
            print('实际:          消耗异常: ', int(x), '!=', int(y), '+', int(mOperate['cost_num']))
            return False
#对比控件内字符串与保存的临时文件是否包含
def diff_strs(mOperate, cts):
    time.sleep(3)
    x = gt.getTxt(temp_file)
    y = elements_by(mOperate, cts).text
    try:
        assert_that(str(x)).is_subset_of(str(y))
        print('预期:          ', str(x), '=', str(y))
        return True
    except AssertionError as e:
        print('预期:          文本不一致: ', str(x), '!=', str(y))
        return False
# 手势向左侧滑动
def opreate_swipe_left(mOperate, cts):
    time.sleep(1)
    print('预期:          手势向左侧滑动')
    l = getSize(cts)
    for i in range(int(mOperate["num"])):
        cts.driver.swipe(l[0] / 0.75, l[1] / 2, l[0] / 0.55, l[1] / 2, 1500)
# 手势向右侧滑动
def opreate_swipe_right(mOperate, cts):
    time.sleep(1)
    print('预期:          手势向右侧滑动')
    l = getSize(cts)
    for i in range(int(mOperate["num"])):
        cts.driver.swipe(l[0] / 0.55, l[1] / 2, l[0] / 0.75, l[1] / 2, 1500)
# 手势向下拉
def opreate_swipe_down(mOperate, cts):
    time.sleep(1)
    print('预期:          手势向下拉')
    l = getSize(cts)
    for i in range(int(mOperate["num"])):
        cts.driver.swipe(l[0] / 2, l[1] * 0.55, l[0] / 2, l[1] * 0.75, 1500)
# 手势向上推
def opreate_swipe_up(cts, mOperate):
    time.sleep(1)
    print('预期:          手势向上推')
    l = getSize(cts)
    for i in range(int(mOperate["num"])):
        cts.driver.swipe(l[0] / 2, l[1] * 0.75, l[0] / 2, l[1] * 0.55, 1500)
#获取屏幕 width & height
def getSize(cts):
    width = cts.driver.get_window_size()["width"]
    height = cts.driver.get_window_size()["height"]
    return (width, height)
#----------------------------------
# 获取当前日期与取到的日期进行对比，成功返回 True，不成功返回 False，只取到日
def getNowday(mOperate, cts):
    print("1")
    system_get_day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    app_get_day = elements_by(mOperate, cts).now_day
    try:
        assert_that(str(mOperate['now_day'])).is_equal_to(str(system_get_day))
        print('预期:          ', system_get_day)
        print('实际:          ', app_get_day)
        return True
    except AssertionError as e:
        print("预期:          不相同: ", e)
        return False
#android系统按键
def system_button(mOperate, cts):
    try:
        print('预期:          按系统键位: ', mOperate['text'])
        cts.keyevent(keycode=mOperate['text'])
        return True
    except:
        return False
#对比toast,暂时没用
def find_toast(mOperate, cts):
    operate_click(mOperate, cts)
    try:
        # print('mOperate["text"]：---->', mOperate['text'])
        WebDriverWait(cts, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "没有消息")))
        return True
    except:
        return False
#通过xpath循环读取列表内容，直到匹配
def comment_region(mOperate, cts):
    # print("1-----1")
    try:
        for i in range(int(mOperate['num'])):
            # print('mOperate["element_info"]:', mOperate['element_info'])
            findstrs = find_strs(mOperate, cts)
            if findstrs == False:
                strs = mOperate['element_info']
                print(str)
                x = re.sub("\D", "", strs.split('=')[-1].split(']')[0])
                y = str(int(x) + 1)
                x = 'index=\'' + x + '\''
                y = 'index=\'' + y + '\''
                # print('strs-->', strs)
                mOperate['element_info'] = strs.replace(x, y)

            else:
                return True
    except:
        return False
