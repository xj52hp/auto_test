# -*- coding: utf-8 -*-

from api.PO.variable import GetVariable as common
from api.PO.operateurl import Getoperateurl as gou
from api.PO.json import Getjson as gs
import requests
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
temp_file = "./Casetemp.txt"

class OperateElement():

    def request_method(self, mOperate):
        dict = {
            common.GET: lambda: request_get(self, mOperate),
            common.POST: lambda: request_post(self, mOperate)
        }
        return dict[mOperate['request_method']]()
def request_get(cts, mOperate):
        url = gou.get_operateurl(cts, mOperate)
        return gs.get_json(cts, mOperate, requests.get(url).text)

def request_post(cts, mOperate):
        url = gou.get_operateurl(cts, mOperate)
        print(requests.post(url).text)