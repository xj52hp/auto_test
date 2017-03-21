# -*- coding: UTF-8 -*-
import os,codecs
import hashlib
import random
from urllib import request,parse

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def get_md5(x):
    m = hashlib.md5(x.encode(encoding='utf-8'))
    return str(m.hexdigest())



def exec():



def getTxt(homeyaml):
    try:
        f = codecs.open(homeyaml, "r", encoding='utf-8')
        x = f.read()
        f.close()
        return x
    except FileNotFoundError:
        print("找不到文件")
        return False


def get_random():
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    resultList = random.sample(range(0, 8), 8)
    resultList = str(resultList[0]) + str(resultList[1]) + str(resultList[2]) + str(resultList[3]) + str(resultList[4]) + str(resultList[5]) + str(resultList[6]) + str(resultList[7])

    return resultList

exec()


