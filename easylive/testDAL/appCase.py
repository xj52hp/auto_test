
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

        gh = operateYaml.getYam(f)
        for i in gh:
            _operate = bo.OperateElement.operate_element(self, mOperate=i)
            print('i---->', i, '_operate----->', _operate)
            time.sleep(2)
            if _operate is False:
                print('join _operate is False!!!')
                if i['case_name'] is True and i['case_name'] == "frist_login":
                    print('call testLogin_Out---->')
                    lo.testLogin_Out.test_login(self)
                else:

                    print('执行用例出现错误!!!')
                    break
        print('over---->')



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
