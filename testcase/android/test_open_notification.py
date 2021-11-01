# -*- coding: utf-8 -*-
# @Time    : 2021/10/01 18:32
# @Author  : Zhujungui
# @FileName: test_open_notification.py
# @Software: PyCharm
import time,os
from krunner.utils import adb,logger
from testcase.krunner import KRunner
from krunner.conf import get_config_value
from krunner.plugins.login import LoginTool
from pageobjects.android.privacy_popup import PrivacyPopup
from pageobjects.android.open_notification import Open_Notification


class TestOpenPush(KRunner):
    '''
    设置页添加开启引导
    '''
    def setUp(self):
        logger.info('启动app')
        adb.start_schema(get_config_value('serialno')[0],get_config_value('home_scheme'))
        time.sleep(2)
        logger.info('判断隐私协议')
        PrivacyPopup.agree_button.click_if_exist()
        self.driver.watch_alert()
        time.sleep(3)
        logger.info('判断是否登录')
        LoginTool().check_login()
        # 没有登录，开始登录
        LoginTool().login(code="+86", phone_num="13313571109", password="123123mz", type='cmdline')
        self.driver.watch_alert()
        time.sleep(3)
        logger.info('左滑操作')
        Open_Notification.setmenu_Btn.swipe_right_element(1,1)

    def test_open_push(self):
        logger.info('打开侧边栏')
        Open_Notification.setmenu_Btn.click(5)
        logger.info('点击设置按钮')
        Open_Notification.setting_Btn.click(5)
        logger.info('点击通知设置按钮')
        Open_Notification.push_Set.click(5)
        time.sleep(2)
        logger.info('获取截图')
        self.get_sccrenn('/pageobjects/template/bubble.png')
        Open_Notification.message_Btn.click(5)
        self.get_sccrenn('/pageobjects/template/pushPop.png')
        time.sleep(2)
        Open_Notification.close_Btn.click(5)
        Open_Notification.message_Btn.click(5)
        Open_Notification.open_Btn.click(5)
        logger.info('执行完成')


    #获取截图
    def get_sccrenn(self,path):
           # 获取根目录
           curr_dir = os.path.abspath(os.path.join(os.getcwd(), '../..'))
           self.driver.screenshot((curr_dir +path), 30)

