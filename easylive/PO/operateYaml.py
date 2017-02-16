
import yaml
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


# -*- coding:utf-8 -*-
def getYam(homeyaml):
    try:
        with open(homeyaml, encoding='utf-8') as f:
            x = yaml.load(f)
            # print(x)
            return x
    except FileNotFoundError:
        print("找不到文件")


