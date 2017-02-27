
# -*- coding: utf-8 -*-
import os
from selenium.webdriver.support.ui import WebDriverWait
from PO import operateYaml
from PO import operateElement as bo
from TestCase import login_out_phone as lo
import time

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AppCase(object):

    def execCase(self, f):
        time.sleep(20)

        gh = operateYaml.getYam(f)
        for i in gh:
            _operate = bo.OperateElement.operate_element(self, mOperate=i)
            print('i["case_id"]---->', i['case_id'], '_operate----->', _operate)
            time.sleep(1)
            if _operate is False:
                print('join _operate is False!!!')
                fh = fault_Handle(i)
                print('i["element_info"]---->', i['element_info'], 'i["element_info"]---->', i['element_info'], 'fh---->', fh)
                return fh


        print('over---->')
def fault_Handle(i):
    if i['case_name'] == True:
        if i['case_name'] == "frist_login":
            print('call testLogin_Out---->')
            lo.testLogin_Out.test_login()
            return True
        elif i['case_name'] == "room":
            print('go on execcase---->')
            return True
    else:
        print('执行用例出现错误!!!')
        return False



# def getModeList(self, f):
#         bs = []
    #     gh = operateYaml.getYam(f)
    #
    #     for i in range(len(gh)):
    #         print(gh)
    #         self.GetAppCase.find_type = gh[i].get("find_type")
    #         self.GetAppCase.element_info = gh[i].get("element_info")
    #         self.GetAppCase.operate_type = gh[i].get("operate_type")
    #         self.GetAppCase.text = gh[i].get("text")
    #         self.GetAppCase.time = gh[i].get("time")
    #         bs.append(json.loads(json.dumps(self.GetAppCase.to_primitive())))
    #         print(bs)
    #     return bs
