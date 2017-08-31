
# -*- coding: utf-8 -*-
import os
from easyvaas.PO import operateYaml
from easyvaas.PO import operateElement as bo
import time

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AppCase(object):

    def execCase(self, f):
        time.sleep(20)

        gh = operateYaml.getYam(f)
        print(gh)
        for i in gh:
            time.sleep(1)
            if 'text' not in i:
                i['text'] = ''
            if 'case_name' not in i:
                i['case_name'] = ''
            if 'case_id' not in i:
                i['case_id'] = ''

            print("输入：", i['case_id'], i['case_name'], i['operate_type'], i['text'])
            _operate = bo.OperateElement.operate_element(self, mOperate=i)
            print("执行：", _operate)

        print(i['case_name'], 'Case over---->', _operate)
