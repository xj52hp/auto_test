
# -*- coding: utf-8 -*-
import os
from selenium.webdriver.support.ui import WebDriverWait
from PO import operateYaml
from PO import operateElement as bo
from TestCase import login_out_phone as lo

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AppCase(object):

    def execCase(self, f):

        gh = operateYaml.getYam(f)
        for i in gh:
            _operate = bo.OperateElement.operate_element(self, mOperate=i)
            print('i---->', i, '_operate----->', _operate)
            if _operate is False:
                print(i['case_name'])
                if i['case_name'] == "frist_login":
                    #以下注释掉代码解决Android帐号互踢后闪白屏问题
                    # i = gh[0]
                    # bo.OperateElement.operate_element(self, mOperate=i)
                    # print('i-->', i, 'gh[0]-->', gh[0])
                    print('call testLogin_Out---->')
                    lo.testLogin_Out.test_login(self)
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
