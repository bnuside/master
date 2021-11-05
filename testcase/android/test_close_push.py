# -*- coding: utf-8 -*- 
# @Author  :zhujungui
# @Time    :2021/11/3 20:58
# @File    :test_close_push
import time
from pageobjects.android.open_setting_push import OpenSettingPush
from krunner.utils import adb, logger
from testcase.krunner import KRunner
from krunner.conf import get_config_value
from appium.webdriver.webdriver import WebDriver

class TestClosePush(KRunner):

    # 使用方法二需要开启
    # activity = 'com.android.settings/.Settings'

    '''关闭通知'''
    def test_close_push(self):
        self.driver.shell(f'am force-stop {get_config_value("pkg_name")}')
        time.sleep(3)
        # 方法一：通过长按logo进入打开通知
        OpenSettingPush.logo.long_click(3)
        OpenSettingPush.application_push.click(3)

        # 方法二：通过设置页逐级找到快手应用
        '''
        logger.info('打开设置页')
        os.popen(f'adb shell am start -n {self.activity}')
        for i in range(3):
            self.driver.swipe_up()
            time.sleep(1)
            if OpenSettingPush.application_Btn.exist()==True:
                OpenSettingPush.application_Btn.click()
                break
        OpenSettingPush.application_list.click()
        logger.info('判断快手应用是否存在')
        for i in range(3):
            self.driver.swipe_up()
            time.sleep(1)
            if OpenSettingPush.kuaishou_application.exist()==True:
                OpenSettingPush.kuaishou_application.click()
                break
        '''
        OpenSettingPush.push_notification.click(3)
        OpenSettingPush.alow_push.click(3)