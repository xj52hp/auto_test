# -*- coding: utf-8 -*-

from api.PO.variable import GetVariable as common
from api.PO.operateurl import Getoperateurl as gou
from api.PO.josn import Getjosn as gs
import requests
import time,re,os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
temp_file = "./Casetemp.txt"

class OperateElement():

    def request_method(self, mOperate):
        dict = {
            common.GET:request_get(self, mOperate),
            common.POST:request_post(mOperate, self)
        }
def request_get(cts, mOperate):
        url = gou.get_operateurl(cts, mOperate)
        # print(requests.get(url).text)
        gs.get_josn(cts, requests.get(url).text)
def request_post(cts, mOperate):
        url = gou.get_operateurl(cts, mOperate)
        print(requests.post(url).text)