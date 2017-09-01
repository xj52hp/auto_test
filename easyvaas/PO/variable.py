
# 查找元素的方式
class GetVariable(object):
    NAME = "name"
    ID = "id"
    XPATH = "xpath"
    INDEX = "index"
    find_element_by_id = "by_id"
    find_elements_by_id = "by_ids"
    find_element_by_name = "by_name"
    find_elements_by_name = "by_names"
    find_element_by_link_text ="by_link_text"
    find_elements_by_link_text = "by_link_texts"
    find_element_by_xpath = "by_xpath"
    find_elements_by_xpath = "by_xpaths"
    find_element_by_class_name = "class_name"
    find_elements_by_class_name = "class_names"
    SELENIUM = "selenium"
    APPIUM = "appium"
    ANDROID = "android"
    IOS = "ios"
    IE = "ie"
    FOXFIRE = "foxfire"
    CHROME = "chrome"

    CLICK = "click"
    ATTRIBUTES = "attributes"
    #attributes_key 传入元素的属性,例如name id  enabled等,传入的text 如果使用False和True的,请使用F和T或者f和t表示
    DRIVER = ""
    TAP = "tap"
    SWIPELEFT = "swipeLeft"
    SWIPEDOWN = "swipeDown"
    SWIPERIGHT = "swipeRight"
    SWIPEUP = "swipeUp"
    #----mOperate['swipe_com'] == 'ok'则进入滑动循环查找， swipe_com=ok 时，num控制总体滑几屏查找列表几次

    SELENIUM_APPIUM = "appium"

    SEND_KEYS = "send_keys"
    FIND_STR = "find_str"
    FIND_STRS = "find_strs"
    SAVE_STRS = "save_strs"
    DIFF_NUM = "diff_num"
    DIFF_STRS = "diff_strs"
    WAIT_TIME = 20
    SYSTEM_BUTTON = "system_button"
    COMMENT_REGION = "comment_region"
    COMMENT_REGION_FATHER = "comment_region_father"
    FIND_TOAST = "find_toast"
    TEXT_IN_ELEMENT = "text_in_element"
    NOW_DAY = "now_day"

    #selenium
    SEND_CODE = "send_code" # 输入验证码

    #本地存储记录所有的case情况的路径
    SAVE_DIR = "d:/"
    REPORT_INFO_PATH = "d:/info.txt"
    REPORT_INIT = "d:/init.txt"
    REPORT_COLLECT_PATH = "d:/collect.txt"
    CRASH_LOG_PATH = "d:/crash.txt" # 存放crash的json文件名
    #my server
    HOST = '192.168.1.38'
    PORT = 8088

    PROTOCOL = "http://" #协议
    APACHE_PATH = "D:/app/Apache2.2/htdocs/appium/log/" #apapche器的地址，开发可以在这个上面下载异常日志

    SCREEN_IMG_PATH = "D:/app/Apache2.2/htdocs/appium/img/" # 截图地址
    #
    # 各android按键键值
    #     电话键
    #
    #     KEYCODE_CALL 拨号键 5
    #     KEYCODE_ENDCALL 挂机键 6
    #     KEYCODE_HOME 按键Home 3
    #     KEYCODE_MENU 菜单键 82
    #     KEYCODE_BACK 返回键 4
    #     KEYCODE_SEARCH 搜索键 84
    #     KEYCODE_CAMERA 拍照键 27
    #     KEYCODE_FOCUS 拍照对焦键 80
    #     KEYCODE_POWER 电源键 26
    #     KEYCODE_NOTIFICATION 通知键 83
    #     KEYCODE_MUTE 话筒静音键 91
    #     KEYCODE_VOLUME_MUTE 扬声器静音键 164
    #     KEYCODE_VOLUME_UP 音量增加键 24
    #     KEYCODE_VOLUME_DOWN 音量减小键 25
    #
    #     控制键
    #
    #     KEYCODE_ENTER 回车键 66
    #     KEYCODE_ESCAPE ESC键 111
    #     KEYCODE_DPAD_CENTER 导航键 确定键 23
    #     KEYCODE_DPAD_UP 导航键 向上 19
    #     KEYCODE_DPAD_DOWN 导航键 向下 20
    #     KEYCODE_DPAD_LEFT 导航键 向左 21
    #     KEYCODE_DPAD_RIGHT 导航键 向右 22
    #     KEYCODE_MOVE_HOME 光标移动到开始键 122
    #     KEYCODE_MOVE_END 光标移动到末尾键 123
    #     KEYCODE_PAGE_UP 向上翻页键 92
    #     KEYCODE_PAGE_DOWN 向下翻页键 93
    #     KEYCODE_DEL 退格键 67
    #     KEYCODE_FORWARD_DEL 删除键 112
    #     KEYCODE_INSERT 插入键 124
    #     KEYCODE_TAB Tab键 61
    #     KEYCODE_NUM_LOCK 小键盘锁 143
    #     KEYCODE_CAPS_LOCK 大写锁定键 115
    #     KEYCODE_BREAK Break/Pause键 121
    #     KEYCODE_SCROLL_LOCK 滚动锁定键 116
    #     KEYCODE_ZOOM_IN 放大键 168
    #     KEYCODE_ZOOM_OUT 缩小键 169
    #
    #     组合键
    #
    #     KEYCODE_ALT_LEFT Alt+Left
    #     KEYCODE_ALT_RIGHT Alt+Right
    #     KEYCODE_CTRL_LEFT Control+Left
    #     KEYCODE_CTRL_RIGHT Control+Right
    #     KEYCODE_SHIFT_LEFT Shift+Left
    #     KEYCODE_SHIFT_RIGHT Shift+Right
    #
    #     基本
    #
    #     KEYCODE_0 按键'0' 7
    #     KEYCODE_1 按键'1' 8
    #     KEYCODE_2 按键'2' 9
    #     KEYCODE_3 按键'3' 10
    #     KEYCODE_4 按键'4' 11
    #     KEYCODE_5 按键'5' 12
    #     KEYCODE_6 按键'6' 13
    #     KEYCODE_7 按键'7' 14
    #     KEYCODE_8 按键'8' 15
    #     KEYCODE_9 按键'9' 16
    #     KEYCODE_A 按键'A' 29
    #     KEYCODE_B 按键'B' 30
    #     KEYCODE_C 按键'C' 31
    #     KEYCODE_D 按键'D' 32
    #     KEYCODE_E 按键'E' 33
    #     KEYCODE_F 按键'F' 34
    #     KEYCODE_G 按键'G' 35
    #     KEYCODE_H 按键'H' 36
    #     KEYCODE_I 按键'I' 37
    #     KEYCODE_J 按键'J' 38
    #     KEYCODE_K 按键'K' 39
    #     KEYCODE_L 按键'L' 40
    #     KEYCODE_M 按键'M' 41
    #     KEYCODE_N 按键'N' 42
    #     KEYCODE_O 按键'O' 43
    #     KEYCODE_P 按键'P' 44
    #     KEYCODE_Q 按键'Q' 45
    #     KEYCODE_R 按键'R' 46
    #     KEYCODE_S 按键'S' 47
    #     KEYCODE_T 按键'T' 48
    #     KEYCODE_U 按键'U' 49
    #     KEYCODE_V 按键'V' 50
    #     KEYCODE_W 按键'W' 51
    #     KEYCODE_X 按键'X' 52
    #     KEYCODE_Y 按键'Y' 53
    #     KEYCODE_Z 按键'Z' 54

