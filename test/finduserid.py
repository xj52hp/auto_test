# coding=utf-8
import xlrd
import json
import requests
import time
import openpyxl

def excel_write(MobilePhone, UserId, inpath, i):

    data = openpyxl.load_workbook(inpath)
    sheet1 = data.worksheets[0]
    print(MobilePhone)
    print(UserId)

    # excel中单元格为B2开始，即第2列，第2行
    sheet1.cell(i + 1, 5).value = UserId

    data.save(inpath)



def json_data(data, i):

    json_str = json.dumps(data)
    data1 = json.loads(json_str)
    print(data1)
    # print(data1['result'])
    try:
        json_str1 = json.dumps(data1['result'])
        data2 = json.loads(json_str1)
        MobilePhone = str(data2['MobilePhone'])
        UserId = str(data2['UserId'])
        excel_write(MobilePhone, UserId, inpath, i)
    except:
        excel_write('10000', '', inpath, i)

def post(MobilePhone, i):

        url = 'http://user.api.autohome.com.cn/api/userInfo/getuserInfobymobilephone'
        p={'_appid':'user', 'MobilePhone':MobilePhone}
        r = requests.post(url, data=p)
        result = {}
        if r.status_code == 200:
            result = json.loads(r.text)
        result["status_code"] = r.status_code
        json_data(result, i)


def extract(inpath):
    data = xlrd.open_workbook(inpath, encoding_override='utf-8')
    table = data.sheets()[0]  # 选定表
    nrows = table.nrows  # 获取行号
    ncols = table.ncols  # 获取列号

    for i in range(1, nrows):  # 第0行为表头
        alldata = table.row_values(i)  # 循环输出excel表中每一行，即所有数据
        MobilePhone = str(alldata[1])[:-2]  # 取出表中第二列数据
        print(i)
        time.sleep(1)

        post(MobilePhone, i)


inpath = '/Users/lishuangqing2019/Desktop/66.xlsx' # excel文件所在路径
extract(inpath)
