import time

from krunner.conf import get_config_value
from krunner.core.android.element import AndroidElement
from krunner.runner import Runner
from krunner.utils import logger, adb


class LoginUtil(Runner):

    @staticmethod
    def initial_page_login_account(phone, pwd):
        """
        手机号登录功能
        :param phone:手机号
        :param pwd:密码
        :return:
        """
        AndroidElement(text='请输入手机号', annotation='输入手机号').input_text(phone)
        AndroidElement(text='密码登录', annotation='密码登录').click()
        time.sleep(2)
        AndroidElement(xpath='//*[@resource-id="com.kuaishou.nebula:id/user_phone_num_info"]',
                       annotation='密码输入框').input_text(pwd)
        AndroidElement(xpath='//*[@resource-id="com.kuaishou.nebula:id/protocol_checkbox"]',
                       annotation='同意隐私文案').click()
        AndroidElement(text='登录', annotation='登录').click()
        time.sleep(2)

    def show_settings_page_but(self):
        logger.info('进到设置页面')
        adb.start_schema(get_config_value('serialno')[0], 'ksnebula://settings')

        logger.info('滑动页面')
        self.driver.swipe_up(0.9, 0.1)
        self.driver.swipe_up(0.9, 0.1)
        time.sleep(2)

    def operation_input_phone(self):
        """
        提供给登录优化需求，防止键盘切换到IME后，无法再次吊起系统键盘
        """
        self.driver.tap_by_screen_percent(0.282, 0.76)
        self.driver.tap_by_screen_percent(0.496, 0.823)
        self.driver.tap_by_screen_percent(0.494, 0.762)
        self.driver.tap_by_screen_percent(0.496, 0.96)
        self.driver.tap_by_screen_percent(0.282, 0.76)
        self.driver.tap_by_screen_percent(0.494, 0.891)
        self.driver.tap_by_screen_percent(0.494, 0.891)
        self.driver.tap_by_screen_percent(0.714, 0.888)
        self.driver.tap_by_screen_percent(0.498, 0.824)
        self.driver.tap_by_screen_percent(0.498, 0.76)
        self.driver.tap_by_screen_percent(0.28, 0.825)



