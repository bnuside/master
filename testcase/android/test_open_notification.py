# -*- coding: utf-8 -*-
# @Time    : 2021/10/31 18:32
# @Author  : Zhujungui
# @FileName: test_open_notification.py
# @Software: PyCharm
import time, os
from krunner.utils import adb, logger
from testcase.krunner import KRunner
from krunner.conf import get_config_value
from krunner.plugins.login import LoginTool
from pageobjects.android.privacy_popup import PrivacyPopup
from pageobjects.android.open_notification import Open_Notification

class TestOpenPush(KRunner):
    '''
    设置页添加push开关
    '''

    def setUp(self):
        logger.info('启动app')
        adb.start_schema(get_config_value('serialno')[0],'kwai://myprofile')
        # time.sleep(2)
        # logger.info('判断隐私协议')
        # PrivacyPopup.agree_button.click_if_exist()
        # self.driver.watch_alert()
        # time.sleep(3)
        # logger.info('判断是否登录')
        # LoginTool().check_login()
        # # 没有登录，开始登录
        # LoginTool().login(code="+86", phone_num="13313571109", password="123123mz", type='cmdline')
        # self.driver.watch_alert()
        time.sleep(3)
        logger.info('左滑操作')
        Open_Notification.setmenu_Btn.swipe_right_element(1, 2)

    # 整个流程：设置页打开——出现气泡和弹窗
    def test_open_push(self):
        self.common()
        logger.info('获取截图')
        self.get_screen('/bubble.png')
        Open_Notification.message_Btn.click(5)
        self.get_screen('/pushPop.png')
        time.sleep(2)
        Open_Notification.close_Btn.click(5)
        Open_Notification.message_Btn.click(5)
        Open_Notification.open_Btn.click(5)
        time.sleep(2)
        Open_Notification.turn_on.click(5)
        self.driver.back()
        self.get_screen('/openPush.png')
        logger.info('执行完成')


    # 通知关闭后，设置页总开关出现气泡引导
    def test_bubble_guide(self):
        self.common()
        assert Open_Notification.acceptance_Btn.exist()
        self.get_screen('/bubble.png')


    # 通知关闭后,设置页总开关出现弹窗
    def test_push_popue(self):
        self.common()
        Open_Notification.message_Btn.click(5)
        self.get_screen('/pushPop.png')
        time.sleep(2)
        Open_Notification.close_Btn.click(5)
        Open_Notification.message_Btn.click(5)
        Open_Notification.open_Btn.click(5)
        time.sleep(2)
        Open_Notification.turn_on.click(5)
        self.driver.back()
        time.sleep(2)
        self.get_screen('/openPush.png')


    # 打开设置页操作
    def common(self):
        logger.info('打开侧边栏')
        Open_Notification.setmenu_Btn.click(5)
        logger.info('点击设置按钮')
        Open_Notification.setting_Btn.click(5)
        logger.info('点击通知设置按钮')
        Open_Notification.push_Set.click(5)
        time.sleep(2)

    # 获取截图
    def get_screen(self, path):
        # 获取根目录
        curr_dir = os.path.abspath(os.path.join(os.getcwd(), '../../pageobjects/template/push'))
        self.driver.screenshot((curr_dir + path), 30)
