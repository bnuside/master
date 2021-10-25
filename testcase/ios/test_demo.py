#!/usr/bin/env python3
import time
from krunner.utils import logger

from pageobjects.ios.main_page import MainPage
from testcase.krunner import KRunner


class TestDemo(KRunner):
    """快手ios端demo演示"""

    def test_demo(self):
        """demo用例"""
        logger.info("等待启动完成，闪屏加载完成")
        time.sleep(5)
        self.driver.swipe_up()
        MainPage.btn_find.click()
        MainPage.btn_guanzhu.click()
        MainPage.tab_recrod.click()
        # ...
        self.assert_equal('测试xxx功能', True, True)