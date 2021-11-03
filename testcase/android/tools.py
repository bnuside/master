# -*- coding: utf-8 -*- 
# @Author  :zhujungui
# @Time    :2021/11/3 20:58
# @File    :tools
# oppo手机打开设置通知
import time,os
from pageobjects.android.open_setting_push import OpenSettingPush
from krunner.utils import adb, logger
from testcase.krunner import KRunner
from krunner.conf import get_config_value

class Tools(KRunner):
    '''不同厂商打开通知'''

    def oppo(self):
        self.driver.shell('')
    # 获取屏幕大小
    def get_screenSize(self):
        x = self.get_window_size()['width']
        y = self.get_window_size()['height']
        return (x, y)

    # 像左滑动
    def swipeLeft(self):
        logger.info('swipeLeft ')
        l = self.get_screenSize()
        y1 = int(l[1] * 0.5)
        x1 = int(l[0] * 0.95)
        x2 = int(l[0] * 0.25)
        self.swipe(x1, y1, x2, y1, 1000)

    # 像下活动
    def swipeDown(self):
        logger.info('swipeDown ')
        l = self.get_screenSize()
        y1 = int(l[1] * 0.5)
        x1 = int(l[0] * 0.95)
        y2 = int(l[1] * 0.25)
        self.swipe(x1, y1, x1, y2, 1000)