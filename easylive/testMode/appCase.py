
from schematics.models import Model
from schematics.types import StringType,IntType

class GetAppCase(Model):
    element_info = StringType() # (查找类型：name/id/xpah)
    operate_type = StringType() #具体的详情,如xpath:“/android.widget.TextView[contains(@text,'Add note'")）,id等
    msg = StringType() # 输入的内容
    find_type = StringType() # 操作类型。比如点击，下拉，拖动等等，对应common
    time = IntType() # 配合与滑动操作
    name = StringType()
    index = IntType()
    text = StringType()# 输入信息
    log = StringType() # 本地log信息路径，一般由手机名字_型号构成