#coding=utf-8
import random
import time
import traceback
import appium_ecloud


def auto_interact(driver):
    activity = driver.current_activity
    # 一定的机率滑动，返回键，点击
    rate = random.random()
    if rate < 0.1:
        print activity + ' Scroll Down'
        appium_ecloud.test_scroll_down(driver)
    elif rate < 0.2:
        print activity + ' Scroll Up'
        appium_ecloud.test_scroll_up(driver)
    elif rate < 0.3:
        print activity + ' Key Back'
        driver.press_keycode(4)
    else:
        btn_list = driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
        if (len(btn_list) > 0):
            index = random.randint(0, len(btn_list) - 1)
            print activity + ' Click Button index = %d' % (index,)
            btn_list[index].click()


def main():
    driver = None
    try:
        driver = appium_ecloud.install_app()
        time.sleep(appium_ecloud.LONG_WAIT_TIME)
        appium_ecloud.agree_document(driver)
        appium_ecloud.quick_login(driver)
        step = 0
        while step < 100:
            if (driver.current_activity.endswith('LoginActivity')):
                appium_ecloud.test_login(driver)
            elif (driver.current_activity.endswith('.Launcher')):
                driver.background_app(1)
                driver.launch_app()
            else:
                auto_interact(driver)
                time.sleep(appium_ecloud.CLICK_WAIT_TIME)
            step += 1
        # 正常退出
        driver.quit()

    except Exception, e:
        print Exception, ":", e
        traceback.print_exc()
        # 异常退出
        if (driver != None):
            driver.quit()


if __name__ == '__main__':
    for i in range(20000):
        try:
            main()
        except Exception, e:
            print Exception, ":", e
            traceback.print_exc()