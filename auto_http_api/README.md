#��Ŀ�������
����python3���Զ����ӿڲ��Կ��

# ����
* Win7 64��python 3��Pycharm. unittest
* xml��������
* �ʼ����Ͳ��Խ��

# �÷�
* Runner_m.py ���Ĵ��롣run_case�ǳ�������
* ����xml

```
<root>
    <title>�ӿڲ���</title>
    <host>ddd.XX.com</host>
    <port>80</port>
    <No>[1001]</No> #  �����������������������
    <header>{"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:29.0) Gecko/20100101 Firefox/29.0"}</header>
    <InterfaceList>
        <params>
            <name type="str">account</name>
            <value>1361212121</value>
            <must>1</must>
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
        <isList>0</isList>
        <id>1001</id>
        <name>��½</name>
        <method>POST</method>
        <url>Login</url>
        <hope>{"appStatus":{"errorCode":0,"message":"����...</hope>
        <login>user_id</login> # ��½����Ҫ���ص���Ϣ�������ӿڵ��ã�����userid,token��
        <isList>0</isList>
    </InterfaceList>
    <InterfaceList>
      <params>
            <name type="int">lookerId</name>
            <value>2</value>
            <must>1</must>
        </params>
        <id>1002</id>
        <name>������ҳ</name>
        <method>GET</method>
        <url>GetPersonalHomePage1</url>
        <hope>{"appStatus":{"errorCode":0,"message":"�����ɹ�"},"content":[{"business_name":"�������","notice_img":"\/product\/20160718184134_321.jpg","user_type":1,"user_id":2,"goods":[{"good_price":45211.0,"good_id":12,"good_name":"��ŷ","banner_picture1":"\/product\/20160719165135_8977.png"},{"good_price":199.0,"good_id":14,"good_name":"�����1","banner_picture1":"\/product\/20160720102028_5352.jpg"},{"good_price":452.0,"good_id":6,"good_name":"ʵ����Ʒ","banner_picture1":"\/product\/20160718165448_2602.png"},{"good_price":99898.0,"good_id":11,"good_name":"Խ��â��","banner_picture1":"\/product\/20160720100057_5877.jpg"}],"shop_img":"\/product\/20160718120144_3196.jpg","head_picture":"http:\/\/dgm.boweixin.com\/\/product\/20160718134528_4744.jpg","notice_id":1}]}</hope>
         <login>1</login> # ��Ҫ��½��Ĳ���
        <isList>1</isList> # ��Ƕ�ײ�
    </InterfaceList>
</root>


ע������,�������֤�����ֵ�����ͻ��߷Ǳ��������Ԥ��ֵע��仯
  <params>
            <name type="str">account</name> # type=str��ʾ�ַ�����
            <value>18576759587</value>
            <must>1</must> # 1��ʾ���0�Ǳ���
        </params>

```

## ���ڼ���

��Ƕ�ײ㡣�������ǣ�����һ���code,�ڶ���list��key�Ƿ���ȣ�list��value��ֵ��type�Ƿ����

# ʹ�ñ���

![test_mark.png](img/test_mark.png "test_mark.png")

![test_detail.png](img/test_detail.png "test_detail.png")

# ����

* ������Ϣ�鿴�ҵ�[������־](channel_log.md)
* ֮ǰд��[�ӿ�����������](https://github.com/284772894/SaveXML)����xml
