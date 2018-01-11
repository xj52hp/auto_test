# -*- coding: utf-8 -*-
import pickle

import subprocess
import shutil
import threading

from multiprocessing import Process

from monkeyTest_double.Base.BasePickle import writeInfo, writeSum, readInfo
from monkeyTest_double.Base.BaseWriteReport import report

import datetime
import uuid
import time
from multiprocessing import Pool

from monkeyTest_double.Base.BaseFile import OperateFile
import os
from monkeyTest_double.Base import AdbCommon
from monkeyTest_double.Base import BaseMonkeyConfig

from monkeyTest_double.Base import BasePhoneMsg
from monkeyTest_double.Base import BaseMonitor

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

ba = AdbCommon.AndroidDebugBridge()


info = []
info_dir = "info/"
log_dir = "log"

# 手机信息
def get_phome(devices):
    bg = BasePhoneMsg.get_phone_Kernel(devices)
    app = {}
    app["phone_name"] = bg[0]["phone_name"] + "_" + bg[0]["phone_model"] + "_" + bg[0]["release"]
    app["pix"] = bg[3]
    app["rom"] = bg[1]
    app["kel"] = bg[2]
    return app


def mkdirInit(devices, app, data=None):
    # destroy(devices)
    cpu = PATH(info_dir + devices + "_cpu.pickle")
    men = PATH(info_dir + devices + "_men.pickle")
    flow = PATH(info_dir + devices + "_flow.pickle")
    battery = PATH(info_dir + devices + "_battery.pickle")
    fps = PATH(info_dir + devices + "_fps.pickle")
    app[devices] = {"cpu": cpu, "men": men, "flow": flow, "battery": battery, "fps": fps, "header": get_phome(devices)}
    OperateFile(cpu).mkdir_file()
    OperateFile(men).mkdir_file()
    OperateFile(flow).mkdir_file()
    OperateFile(battery).mkdir_file()
    OperateFile(fps).mkdir_file()
    OperateFile(PATH(info_dir + "sumInfo.pickle")).mkdir_file() # 用于记录是否已经测试完毕，里面存的是一个整数
    OperateFile(PATH(info_dir + "info.pickle")).mkdir_file() # 用于记录统计结果的信息，是[{}]的形式

    writeSum(0, data, PATH(info_dir + "sumInfo.pickle")) # 初始化记录当前真实连接的设备数

def runnerPool():

    devices_Pool = []
    devices = ba.attached_devices()
    if devices:
        for item in range(0, len(devices)):
            _app = {}
            _app["devices"] = devices[item]
            _app["num"] = len(devices)
            devices_Pool.append(_app)
        pool = Pool(len(devices))
        pool.map(start, devices_Pool)
        pool.close()
        pool.join()
    else:
        print("设备不存在")


def start(devicess):
    devices = devicess["devices"]
    num = devicess["num"]
    app = {}
    print("devices---->", devices)
    print("num---->", num)
    print("app---->", app)
    mkdirInit(devices, app, num)
    mc = BaseMonkeyConfig.monkeyConfig(PATH("monkey.ini"))
    # 打开想要的activity
    # ba.open_app(mc["package_name"], mc["activity"], devices) 留着备用可以统计每次打开哪个页面的启动时间等
    # monkey开始测试
    mc["log"] = PATH(log_dir) + "\\" + str(uuid.uuid4())
    mc["monkey_log"] = mc["log"] + "monkey.log"
    mc["cmd"] = mc['cmd'] + mc["monkey_log"]
    start_monkey("adb -s " + devices + " shell " + mc["cmd"], mc["log"])
    time.sleep(1)
    starttime = datetime.datetime.now()
    pid = BaseMonitor.get_pid(mc["package_name"], devices)
    cpu_kel = BaseMonitor.get_cpu_kel(devices)
    beforeBattery = BaseMonitor.get_battery(devices)
    while True:
        with open(mc["monkey_log"], encoding='utf-8') as monkeylog:
            time.sleep(1)  # 每1秒采集检查一次
            BaseMonitor.cpu_rate(pid, cpu_kel, devices)
            BaseMonitor.get_men(mc["package_name"], devices)
            BaseMonitor.get_fps(mc["package_name"], devices)
            BaseMonitor.get_flow(pid, mc["net"], devices)
            BaseMonitor.get_battery(devices)
            if monkeylog.read().count('Monkey finished') > 0:
                endtime = datetime.datetime.now()
                print(str(devices)+"测试完成咯")
                writeSum(1, path=PATH(info_dir + "sumInfo.pickle"))
                app[devices] ["header"]["beforeBattery"] = beforeBattery
                app[devices]["header"]["afterBattery"] = BaseMonitor.get_battery(devices)
                app[devices]["header"]["net"] = mc["net"]
                app[devices]["header"]["monkey_log"] = mc["monkey_log"]
                app[devices]["header"]["time"] = str((endtime - starttime).seconds) + "秒"
                writeInfo(app, PATH(info_dir + "info.pickle"))
                break
                    # go.info[devices]["header"]["sumTime"] = str((endtime - starttime).seconds) + "秒"
                    # report(go.info)
    if readInfo(PATH(info_dir + "sumInfo.pickle")) <= 0:
        print(readInfo(PATH(info_dir + "info.pickle")))
        report(readInfo(PATH(info_dir + "info.pickle")))
        subprocess.Popen("taskkill /f /t /im adb.exe", shell=True)
        # shutil.rmtree((PATH(info_dir))) # 删除持久化目录
        print("------来吧------")


# 开始脚本测试
def start_monkey(cmd, log):
    # Monkey测试结果日志:monkey_log
    os.popen(cmd)
    print(cmd)

    # Monkey时手机日志,logcat
    logcatname = log + r"logcat.log"
    cmd2 = "adb logcat -d >%s" % (logcatname)
    os.popen(cmd2)

    # "导出traces文件"
    tracesname = log + r"traces.log"
    cmd3 = "adb shell cat /data/anr/traces.txt>%s" % tracesname
    os.popen(cmd3)

def killport():
    os.system(PATH('./kill5037.bat'))
    os.popen("adb kill-server adb")
    os.popen("adb start-server")

def init_dir():
    if os.path.exists(info_dir):
        shutil.rmtree(info_dir)  # 删除持久化目录
    os.makedirs(PATH(info_dir))  # 创建持久化目录
    if os.path.exists(log_dir):
        shutil.rmtree(log_dir)  # 删除持久化目录
    os.makedirs(PATH(log_dir))  # 创建持久化目录


if __name__ == '__main__':
    #killport()
    time.sleep(1)
    init_dir()
    runnerPool()
    # p = Process(target=runnerPool, args=())
    # p.start()
    # p.join()