#����python3ʵ�ֵ�http�ӿ��Զ�������

##��������
* Win7 64��python 3��Pycharm. unittest
* ��ȡ�����ļ�--��ȡ��������--ִ�в�������--��¼���Խ��--����html����ļ�

##��ܼ��
* ֧�ֳ�����HTTP�е�post��get����
* ���԰���������excel����ע��ĵط���Ϊÿ�����������Զ����麯��������Ϊ��������Ϊxml����
* ������Ҫ���ã��������в���������ȫ������
* ���Խ�����������html�ļ�������鿴��


##ģ��������˵��
* Httpbase.py ��ȡhttp�������Ͷ˿�
* Config.py http�����ķ�װ,����֧�ֶ�Э����չ��get,post
* Runner_m.py ���Ĵ��롣run_case�ǳ�������
* Htmlreport.py �������html�ļ�
![������ɱ���](img/report.png  "������ɱ���")

##��Ҫ������ʷ��

###2015-8-3 ������ʷ
* �Զ����ӿڲ��Կ�����
* ����������pyh(���ɽ��html�ļ�), config.ini������Ϣ  excel��������
![testCaseExcel.xlsl](img/testCaseExcel.png "testCaseExcel.xlsl")
``` �����ļ�
Case_config.ini
[DEFAULT]
index = [1001,1002] �������в�������id
host = 192.168.1.249
port = 10003
```

![������ɱ���](img/report.png  "������ɱ���")

###2016-1-5 ������־
* ������ʹ����requestsģ�飬�����Զ�����չ��get,post,put,delete,head,options�ȷ�����ͬʱ֧���ϴ�ͼƬ
* ��������excel���������������ʹ��html����xml�ӿ��ļ��󣬸�python������.

###2016-1-8 ������־
* �޸���֧��ָ�����Խӿڲ���id

###2016-1-9 ������־
* �Ż���html������xml�ӿڣ�ֻҪ����ӿ����֣��������������Զ��庯���Ϳ�����


###2016-1-12 ������־
* ȥ���Զ�����������ʡ�������룬ֻ���ڽӿ�xml��������ָ��Ԥ�ڽ���Ϳ�����

###2016-1-23 ������־
* ������Ԥ�ڽ��ż���޷����ɹ���bug
* ��������Ҫ��½���id����token����ʹ�ýӿ�

###2016-3-22 ������־
* �Ż��˼��㡣���ʵ�ʽ��������Ƕ�ײ㣬����ֻҪ���ʵ�ʽ����Ƕ�ײ�ĵ�һ��������:data[{"a":b},{"a":"c"}].ֻҪ���{"a":"b"}
 * һ������Ͷ������㣨Ƕ�ײ㣬ֻ�Ǽ��key�Ƿ���ڣ�
 * ���������Ҫ�õ���list set��ķ�ʽ 
* ������html�ӿ�������

* ����������ο���https://github.com/284772894/SaveXML

### 2016-7-21

* ������Ż�����
* ��Ҫ�����˶Աȹ���,��һ��Ա�code��״̬���ڶ���ȫ�ֶζԱȣ�֮ǰ�븴����

```
def compare(exJson,factJson):
    if factJson["appStatus"]["errorCode"] == 0:
       return exJson==factJson
    else:
        print("�ӿ�����ʧ��")
        return False
```


### 2016-7-30 ������־
* �޸ĶԱȹ��������Ƕ�ײ㣬��ҳ�Աȵ�һ���code,Ȼ��Ա�����Ƕ�ײ��value������������Ƕ�ײ��ȫ�ֶ�ƥ��

```
def compare(exJson,factJson,isList=0):
    isFlag = True
    if exJson.get("appStatus") == factJson.get("appStatus"):
        if isList== False: # ���û��Ƕ�ײ�
            return isFlag
        data2 = exJson.get("content")
        data3 = factJson.get("content")
        for item2 in data2:
            for item3 in data3:
                keys2 = item2.keys()
                keys3 = item3.keys()
                if keys2 == keys3: # ���Ƕ�ײ��key��ȫ���
                     for key in keys2:
                        value2 = item2.get(key)
                        value3 = item3.get(key)
                        if type(value3)==type(value2):# �Ա�Ƕ�ײ��value��typeֵ
                           pass
                        else:
                            isFlag = False
                            break
                else:
                    isFlag = False
                    break
    else:
        isFlag = False
    print(isFlag)
    return isFlag
```

### 2016-8-22 ������־

* ���Ա�����ÿ���excel����ʾ��ʽ 

![test_mark.png](img/test_mark.png "test_mark.png")

![test_detail.png](img/test_detail.png "test_detail.png")

### 2016-8-23 ������־

* ���Ա����Է����ʼ��ķ�ʽ֪ͨ

### 2016-9-7
* ����ܹ��ع�����ϵͳ

### 2016-9-8
* �����ӿڲ�����չ
	* �������Ƿ����
	* ��������ֵ�����Ƿ���ȷ
	
### 2016-9-9 
* ʵ�ּ������Ƿ����
* ��������ֵ�����Ƿ���ȷ
* ��http_code��ֵ�ϲ���ʵ�ʽ��

```
  <params>
            <name type="str">account</name> # type=str��ʾ�ַ�����
            <value>18576759587</value>
            <must>1</must> # 1��ʾ���0�Ǳ���
        </params>
        <params>
            <name type="str">password</name>
            <value>222222</value>
            <must>1</must>
        </params>
         <params>
            <name type="int">type</name>
            <value>0</value>
            <must>1</must>
        </params>
```


