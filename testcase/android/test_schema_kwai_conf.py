# -*- coding: utf-8 -*- 
# @Author  :zhujungui
# @Time    :2021/11/18 20:28
# @File    :test_schema_kwai_conf

from krunner.utils import logger
from krunner.conf import get_config_value
from testcase.krunner import KRunner
import time,os
from testcase.android.test_open_notification import TestOpenPush
from pageobjects.android.schema_kwai_conf import SchemaKwaiConf

class TestSchemaKwai(KRunner):
    '''快链跳转可配置'''
    TestOpenPush.setUp(phone="13313571109",pasPwd="123123mz")


    def test_live(self):
        logger.info('跳转直播页返回测试')
        for num in range(2, 8):
            self.driver.shell(f'am start -d kwai://live/play/h564uXu6_5M?commonBackHomeTabId={num}')

    def test_work(self):
        pass
    def test_follow(self):
        pass
