# -*- coding: utf-8 -*-

from assertpy import assert_that
import json
from api.PO import operateYaml as oy

class Getjson():
    def get_json(self, mOperate, json_T):
        param = json.loads(json_T)
        print("Json返回参数:    ", str(param))
        try:
            if assert_that(str(param['retval'])).is_equal_to(str(mOperate['retval'])):
                print("实际:            ", str(param['retval']))
                return save_retinfo(self, param)
            else:
                return print("实际:            与预期不符合")
        except AssertionError as e:
            # print(e)
            return False
def save_retinfo(cts, param):

    try:
        param_retinfo = param['retinfo']
        if assert_that(param_retinfo['sessionid']).is_not_empty():
            return oy.writeTxt(json.dumps(param['retinfo']))
        else:
            return print('param_retinfo不存在')
    except AssertionError as e:
        # print(e)
        return print('param_retinfo写入异常')
