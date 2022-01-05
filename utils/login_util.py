import time

from krunner.conf import get_config_value
from krunner.core.android.element import AndroidElement
from krunner.runner import Runner
from krunner.utils import logger, adb

from pageobjects.android.login_optimize_page import LoginOptimizePage
from pageobjects.android.settings_page_login import SettingsPageLogin


class LoginUtil(Runner):

    @staticmethod
    def nebula_initial_page_login_account(phone, pwd, order=1):
        """
        极速版手机号登录功能
        :param phone:手机号
        :param pwd:密码
        :param order:多账号选择哪一个
        :return:
        """
        SettingsPageLogin.initial_page_switch_pwd_login.click()  # 切换到密码登录，防止切换到IME键盘无法输入密码
        time.sleep(2)
        SettingsPageLogin.initial_page_phone_input.input_text(phone)  # 输入手机号
        SettingsPageLogin.nebula_initial_page_pwd_input.input_text(pwd)  # 输入密码
        logger.info('点击同意隐私文案')
        SettingsPageLogin.nebula_initial_page_privacy_agree.click()
        SettingsPageLogin.initial_page_login_but.click()
        time.sleep(2)
        if SettingsPageLogin.nebula_first_account_photo.exist():
            if order == 1:
                SettingsPageLogin.nebula_first_account_photo.click(3)
            elif order == 2:
                SettingsPageLogin.nebula_second_account_photo.click(3)

    def show_settings_page_login_but(self, pkg_name):
        """
        进到设置页面
        :param pkg_name:包名
        """
        if 'com.kuaishou.nebula' == pkg_name:
            logger.info('进到设置页面')
            adb.start_schema(get_config_value('serialno')[0], get_config_value('nebula_schema')[2])
        elif 'com.smile.gifmaker' == pkg_name:
            logger.info('进到设置页面')
            adb.start_schema(get_config_value('serialno')[0], get_config_value('nebula_schema')[2])
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

    @staticmethod
    def smile_initial_page_login_phone_account(phone, pwd, order=1):

        """
        主站手机号手机号登录功能
        :param phone:手机号
        :param pwd:密码
        :param order:多账号选择哪一个
        :return:
        """
        time.sleep(3)
        LoginOptimizePage.pwd_regist_but.click()
        LoginOptimizePage.phone_input_frame.input_text(phone)  # 输入手机号
        LoginOptimizePage.smile_pwd_input_but.input_text(pwd)  # 输入手机号
        logger.info('点击同意隐私文案')
        LoginOptimizePage.smile_privacy_agreement_but.click(2)
        LoginOptimizePage.login_button.click(2)  # 登录
        time.sleep(5)
        if LoginOptimizePage.smile_first_account_photo.exist():
            if order == 1:
                LoginOptimizePage.smile_first_account_photo.click(3)
            elif order == 2:
                LoginOptimizePage.smile_second_account_photo.click(3)
