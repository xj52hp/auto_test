
from easylive.PO.variable import GetVariable as common
from easylive.PO import operateYaml as gt
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium import webdriver
import selenium.common.exceptions
import time,re,os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
temp_file = "./Casetemp.txt"

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
                common.SWIPELEFT: lambda: opreate_swipe_left(mOperate, self.driver),
                common.SWIPEDOWN: lambda: opreate_swipe_down(mOperate, self.driver),
                common.SWIPEUP: lambda: opreate_swipe_up(mOperate, self.driver),
                common.SWIPERIGHT: lambda: opreate_swipe_right(mOperate, self.driver),
                common.FIND_STR: lambda: find_str(mOperate, self.driver),
                common.FIND_STRS: lambda: find_strs(mOperate, self.driver),
                common.SAVE_STRS: lambda: save_strs(mOperate, self.driver),
                common.DIFF_NUM: lambda: diff_num(mOperate, self.driver),
                common.DIFF_STRS: lambda: diff_strs(mOperate, self.driver),
                common.SYSTEM_BUTTON: lambda: system_button(mOperate, self.driver),
                common.COMMENT_REGION: lambda: comment_region(mOperate, self.driver),
                common.FIND_TOAST: lambda: find_toast(mOperate, self.driver)
            }
            return elements[mOperate["operate_type"]]()

        return False
# 点击事件
def operate_click(mOperate, cts):
    if mOperate["find_type"] == common.find_element_by_id or mOperate["find_type"] == common.find_element_by_name or mOperate["find_type"] == common.find_element_by_xpath:
        elements_by(mOperate, cts).click()
    if mOperate["find_type"] == common.find_elements_by_id or mOperate["find_type"] == common.find_elements_by_name:
        elements_by(mOperate, cts)[mOperate["index"]].click()
    if common.SELENIUM_APPIUM == common.APPIUM:
        pass

def send_keys(mOperate, cts):
    try:
        elements_by(mOperate, cts).send_keys(mOperate["text"])
        return True
    except:
        print('输入错误')
        return False

def find_str(mOperate, cts):
    try:
        find_string = elements_by(mOperate, cts).text
        if str(find_string) == str(mOperate['text']):
            print('find_string:', find_string, 'mOperate[text]:', mOperate['text'])
            return True
        else:
            return False
    except:
        print('find_str---->查找错误')
        return None

def find_strs(mOperate, cts):
    find_strings = elements_by(mOperate, cts).text
    print('find_strings:', find_strings, 'mOperate[text]:', mOperate['text'])
    try:
        if str(mOperate['text']) in str(find_strings):
            return True
        else:
            return False
    except:
        print('find_strs---->查找错误')
        return None
def save_strs(mOperate, cts):
    bo = gt.writeTxt(temp_file, elements_by(mOperate, cts).text)
    return bo

def diff_num(mOperate, cts):
        time.sleep(3)
        x = gt.getTxt(temp_file)
        x = re.sub("\D", "", x)
        y = re.sub("\D", "", elements_by(mOperate, cts).text)
        if mOperate['operate_name'] == "roll":
            y = re.sub("\D", "", x)
            x = re.sub("\D", "", elements_by(mOperate, cts).text)

        if int(x) == int(y) + int(mOperate['cost_num']):
            print('变化:---->', int(mOperate['cost_num']))
            return True
        else:
            print('消耗异常:---->', int(x), '!=', int(y), '+', int(mOperate['cost_num']))
            return False
def diff_strs(mOperate, cts):
        time.sleep(3)
        x = gt.getTxt(temp_file)
        y = elements_by(mOperate, cts).text
        if x in y:
            print('内容:---->', str(x), '=', str(y))
            return True
        else:
            print('文本不一致:---->', str(x), '!=', str(y))
            return False


# 手势向左侧滑动
def opreate_swipe_left(mOperate, cts):
    time.sleep(1)
    print('手势向左侧滑动')
    width = cts.get_window_size()["width"]
    height = cts.get_window_size()["height"]
    for i in range(mOperate["time"]):
        cts.swipe(int(width*0.75), int(height*3/4), int(width*0.25), int(height*3/4), 500)
        time.sleep(1)

# 手势向右侧滑动
def opreate_swipe_right(mOperate, cts):
    time.sleep(1)
    print('手势向右侧滑动')
    width = cts.get_window_size()["width"]
    height = cts.get_window_size()["height"]
    for i in range(mOperate["time"]):
        cts.swipe(int(width*0.25), int(height*3/4), int(width*0.75), int(height*3/4), 500)
        time.sleep(1)


# 手势向下拉
def opreate_swipe_down(mOperate, cts):
    time.sleep(1)
    print('手势向下拉')
    width = cts.get_window_size()["width"]
    height = cts.get_window_size()["height"]
    for i in range(mOperate["time"]):
        cts.swipe(int(width/2), int(height*0.25), int(width/2), int(height*0.75), 500)
        time.sleep(1)

# 手势向上推
def opreate_swipe_up(mOperate, cts):
    time.sleep(1)
    print('手势向上推')
    width = cts.get_window_size()["width"]
    height = cts.get_window_size()["height"]
    for i in range(mOperate["time"]):
        cts.swipe(int(width/2), int(height*0.75), int(width/2), int(height*0.25), 500)
        time.sleep(1)

def system_button(mOperate, cts):

    try:
        print('按系统键位：---->', mOperate['text'])
        webdriver.Remote.keyevent(cts, int(mOperate['text']), metastate=None)
        return True
    except:
        return False

def find_toast(mOperate, cts):
    operate_click(mOperate, cts)
    try:
        print('mOperate["text"]：---->', mOperate['text'])
        WebDriverWait(cts, 20, 1).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "没有未读消息")))
        return True
    except:
        return False

#通过xpath循环读取列表内容，直到匹配
def comment_region(mOperate, cts):

    for i in range(7):
        print('mOperate["element_info"]:', mOperate['element_info'])
        findstrs = find_strs(mOperate, cts)
        if findstrs != True:
            strs = mOperate['element_info']
            x = re.sub("\D", "", strs.split('=')[-1].split(']')[0])
            y = str(int(x) + 1)
            x = 'index=\'' + x + '\''
            y = 'index=\'' + y + '\''

            mOperate['element_info'] = strs.replace(x, y)

        else:
            return True
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
        common.find_elements_by_class_name: lambda: cts.find_elements_by_class_name(mOperate['element_info'])[mOperate['index']]
    }
    return elements[mOperate["find_type"]]()