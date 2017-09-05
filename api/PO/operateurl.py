# -*- coding: utf-8 -*-

from api.PO.param import Getparam as gp
from api.PO.serverinfo import Getserverinfo as gsi
from assertpy import assert_that

class Getoperateurl():
    def get_operateurl(self, mOperate):
        serverinfo = gsi.get_serverinfo(self, mOperate)
        param = gp.get_param(self, mOperate)
        print('组合PARAM:         ', param)
        url = serverinfo + mOperate['fun_name'] + '?' + param
        return url