
import yaml
import os,codecs,time

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

def getTxt(homeyaml):
    try:
        f = codecs.open(homeyaml, "r", encoding='utf-8')
        x = f.read()
        f.close()
        return x
    except FileNotFoundError:
        print("找不到文件")
        return False

def writeTxt(temp_file, x):
    try:
        f = codecs.open(temp_file, "w", encoding='utf-8')
        print(x)
        f.write(x)
        f.close()
        time.sleep(2)
        return True
    except FileNotFoundError:
        print("找不到文件")
        return False





