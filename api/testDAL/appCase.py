
# -*- coding: utf-8 -*-
import os
from api.PO import operateYaml
from api.PO import operateElement as bo
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
            if 'request_method' not in i:
                i['request_method'] = 'get'
            if 'server_info' not in i:
                i['server_info'] = 'release'
            try:
                print("接口名称:         ", i['fun_name'])
                print("类型:            ", i['request_method'])
                print("连接服务:         ", i['server_info'])
            except:
                print('请输入case_name&request_method&server_info&fun_name的值')
            _operate = bo.OperateElement.request_method(self, mOperate=i)
            print("执行结果:         ", _operate)
            print("-------------------------")

        print(i['fun_name'], 'Case over---->', _operate)
