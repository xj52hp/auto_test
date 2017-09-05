# -*- coding: utf-8 -*-

from api.PO.variable import GetVariable as common
from assertpy import assert_that

class Getserverinfo():
    def get_serverinfo(self, mOperate):
        try:
            if assert_that(str(common.RELEASE)).is_equal_to(str(mOperate['server_info'])):
                return common.RELEASE_URL
            elif assert_that(str(common.DEV)).is_equal_to(str(mOperate['server_info'])):
                return common.DEV_URL
            elif assert_that(str(common.TEST)).is_equal_to(str(mOperate['server_info'])):
                return common.TEST_URL
            else:
                return print('请写入server_info,默认release')
        except:
            return common.RELEASE_URL
