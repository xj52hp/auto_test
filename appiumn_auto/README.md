# ��Ŀ�������
* ����Ŀ����[appium](https://github.com/appium/appium)��[Selenium](https://github.com/SeleniumHQ/selenium)��Դ���߷�װ���ɵ��Զ���app��web���Թ���

# ����
* ���ǻ���python3
* ���ǻ���webdriver���󲿷ִ��붼����ͨ�ã�ֻ�������ļ���һ��
* APP����˳��õ�men,cpu,fps
* ����ά���õ�YMAL
* �ʼ�����excel�Ĳ��Ա���
* ֧�ֶ��豸andoird����

# �÷�

**������Ŀ:**

```
git clone git@github.com:284772894/appiumn_auto.git
```

**����devices.yaml**

```
appium:
 - devices: JTJ4C16331013562
   port: 4723
   config: node D:\app\Appium\node_modules\appium\bin\appium.js  -p 4723 -bp 4733
   platformName: android
 - devices: MSM8926
   port: 4724
   config: node D:\app\Appium\node_modules\appium\bin\appium.js  -p 4724 -bp 4734
   platformName: android
```

**yaml**

* [case��api](mark.md)

```
--- 
- 
  element_info: cn.ibona.t1_beta:id/start_button
  find_type: by_id
  operate_type: click
  test_id: 1002
  test_intr: ��½
- 
  element_info: cn.ibona.t1_beta:id/passwordEditText
  find_type: by_id
  operate_type: send_keys
  test_id: 1002
  text: 111111
- 
  element_info: cn.ibona.t1_beta:id/phoneNumberEditText
  find_type: by_id
  operate_type: send_keys
  text: 18576759587
- 
  element_info: cn.ibona.t1_beta:id/loginButton
  find_type: by_id
  operate_type: click
- 
  element_info: cn.ibona.t1_beta:id/toolbar
  find_type: by_id

```



**����������:**

```
pyhton testRunner/runner.py
```

# ʹ�ý�ͼ

* ���з�ʽ

![run1.gif](img/run.gif "run.gif")

* APP�������

![run1.gif](img/run1.gif "run1.gif")

* ���չʾ

![testEmail.png](img/testEmail.png "testEmail.png")

![testinit.png](img/testinit.png "testinit.png")

![testReport12-5.png](img/testReport12-5.png "testReport12-5.png")


# ����
* ������Ϣ�鿴�ҵ�[������־](channel_log.md)






