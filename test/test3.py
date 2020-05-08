# coding=utf-8
import xlrd
import json
import requests
import time
import openpyxl


def extract(inpath):
    i = 0
    j = 0
    result = {}
    for i in range(10000):  # 第0行为表头
        print(i)
        url = 'https://ty.autohome.com.cn/app/homepage/channel/t_v10.5.0/recommend?_appid=youji&_rd=ca425fce-590c-4dad-bc74-80bcdcf51508&_source=android&_ts=1587640689044&cityCode=110100&deviceid=5d4aa12d_58af_4e38_b29d_90c324b7b045&operation=0&outmedia=32&sign=51EC19B14620D1AA1066B7EB1A1D5C70&sysType=1&sysVersion=1140&userip=10.169.36.44&version=1'
        r = requests.get(url)
        result = json.loads(r.text)
        data1 = result['result']['recommend']['travelList']

        data2 = data1[1]
        for j in range(len(data1)):
            if int(data2['dataType']) == 20:

                data = openpyxl.load_workbook(inpath)
                sheet1 = data.worksheets[0]
                sheet1.cell(i + 1, 1).value = str(result)

                data.save(inpath)
                print("-------------保存成功-------------")
            else:
                print("没有保存")



inpath = '/Users/lishuangqing2019/Desktop/66.xlsx' # excel文件所在路径
extract(inpath)



def zhonghang():
    way = ''

    if way = 'bus' or way = 'tuizhe'
