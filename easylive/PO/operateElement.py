
from PO.variable import GetVariable as common
from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions
import time

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
            print("找不到数据")
            return False
        except:
            print("找不到数据")
            return False
    def operate_element(self, mOperate):
        if OperateElement.findElement(self, mOperate):
            elements = {
                common.CLICK: lambda: operate_click(mOperate, self.driver),
                common.SEND_KEYS: lambda: send_keys(mOperate, self.driver),
                common.SWIPELEFT: lambda: opreate_swipe_left(mOperate, self.driver),
                common.SWIPEDOWN: lambda: opreate_swipe_down(mOperate, self.driver),
                common.SWIPEUP: lambda: opreate_swipe_up(mOperate, self.driver),
                common.SWIPERIGHT: lambda: opreate_swipe_down(mOperate, self.driver)
                # common.SEND_CODE: lambda: send_code()
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

# 手势向右侧移动
def opreate_swipe_left(mOperate, cts):
    time.sleep(1)
    print('手势向右侧移动')
    width = cts.get_window_size()["width"]
    height = cts.get_window_size()["height"]
    for i in range(mOperate["time"]):
        cts.swipe(int(width/4*3), int(height/2), int(width/4*1), int(height/2), 500)
        time.sleep(1)

# 手势向左侧移动
def opreate_swipe_right(mOperate, cts):
    time.sleep(1)
    print('手势向左侧移动')
    width = cts.get_window_size()["width"]
    height = cts.get_window_size()["height"]
    for i in range(mOperate["time"]):
        cts.swipe(int(width /4*1), int(height/2), int(width/4*3), int(height/2), 500)
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