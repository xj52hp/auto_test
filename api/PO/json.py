# -*- coding: utf-8 -*-

from assertpy import assert_that
import json
from api.PO import operateYaml as oy

class Getjson():
    def get_json(self, mOperate, json_T):
        param = json.loads(json_T)
        try:
            if assert_that(str(param['retval'])).is_equal_to(str(mOperate['retval'])):
                print("实际:            ", str(param['retval']))
                save_retinfo(self, param)
                return True
            else:
                print("实际:            与预期不符合")
                return False
        except AssertionError:
            return False
def save_retinfo(cts, param):

    try:
        param_retinfo = param['retinfo']
        if assert_that(param['retinfo']).is_not_empty() and assert_that(param_retinfo['sessionid']).is_not_in(param_retinfo):
            wr = oy.writeTxt(json.dumps(param['retinfo']))
            if wr is False:
                print('保存文件:          param_retinfo写入异常')
            return True
    except AssertionError:
        return False
