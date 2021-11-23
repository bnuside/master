import time

from krunner.utils import logger
from krunner.utils import adb
from krunner.conf import get_config_value

from pageobjects.android.login_optimize_page import LoginOptimizePage
from pageobjects.android.privacy_popup import PrivacyPopup
from pageobjects.android.settings_page_login import SettingsPageLogin

from testcase.krunner import KRunner
from utils.login_util import LoginUtil


class TestQuitLoginOptimize(KRunner):

    def setUp(self):
        adb.clear_app_data(get_config_value('serialno')[0], get_config_value('pkg_name'))
        time.sleep(2)

        adb.start_schema(get_config_value('serialno')[0], get_config_value('nebula_schema')[0])
        time.sleep(2)

        self.driver.watch_alert()
        time.sleep(7)
        self.driver.watch_alert()
        time.sleep(2)

        adb.start_schema(get_config_value('serialno')[0], get_config_value('nebula_schema')[1])
        time.sleep(2)
        logger.info('点击手机号登录按钮')
        SettingsPageLogin.phone_login_but.click()
        LoginUtil.nebula_initial_page_login_account('17600088922', 'shi123456789')
        LoginUtil.show_settings_page_login_but(self, get_config_value('pkg_name'))  # 进到设置页展示按钮

    def test_settings_page_switch_acount_but(self):
        logger.info('点击设置页切换账号，测试单账号')
        SettingsPageLogin.settings_page_switch_account_but.click()
        logger.info('点击切换账号页面的添加账号')
        SettingsPageLogin.nebula_switch_acount_page_append_account_but.click()
        self.assert_equal('断言添加账号点击成功', LoginOptimizePage.login_button.exist(2), True)
        LoginUtil.nebula_initial_page_login_account('15201889524', 'shi123456789')
        time.sleep(2)
        LoginUtil.show_settings_page_login_but(self, get_config_value('pkg_name'))  # 进到设置页展示按钮

        logger.info('点击设置页切换账号，测试多账号')
        SettingsPageLogin.settings_page_switch_account_but.click()
        logger.info('长按头像')
        SettingsPageLogin.nebula_switch_acount_page_change_acount_first_but.long_click()
        SettingsPageLogin.switch_acount_page_popus_cancel_but.click()
        SettingsPageLogin.nebula_switch_acount_page_change_acount_first_but.long_click()
        logger.info('弹窗的退出点击')
        SettingsPageLogin.switch_acount_page_popus_quit_but.click()
        self.assert_equal('测试弹窗的退出点击成功', SettingsPageLogin.nebula_switch_acount_page_append_account_but.exist(), True)

        logger.info('点击切换账号页面的添加账号,测试切换账号功能')
        SettingsPageLogin.nebula_switch_acount_page_append_account_but.click()
        LoginUtil.nebula_initial_page_login_account('17600088922', 'shi123456789')
        LoginUtil.show_settings_page_login_but(self, get_config_value('pkg_name'))  # 进到设置页展示按钮
        SettingsPageLogin.settings_page_switch_account_but.click()  # 点击设置页的切换账号按钮
        SettingsPageLogin.nebula_switch_acount_page_change_acount_first_but.click()  # 点击头像切换账号
        time.sleep(2)
        self.assert_equal('断言切换账号成功', SettingsPageLogin.switch_acount_page_title.exist(2), False)

        logger.info("点击设置页退出账号，测试退出登录多账号场景")
        LoginUtil.show_settings_page_login_but(self, get_config_value('pkg_name'))
        SettingsPageLogin.settings_page_quit_login_but.click()  # 点击退出账号button
        SettingsPageLogin.settings_page_popus_cancel_but.click()  # 取消弹窗
        SettingsPageLogin.settings_page_quit_login_but.click()
        SettingsPageLogin.settings_page_popus_change_acount_but.click()
        SettingsPageLogin.nebula_switch_acount_page_change_acount_second_but.click()
        LoginUtil.show_settings_page_login_but(self, get_config_value('pkg_name'))
        SettingsPageLogin.settings_page_quit_login_but.click()  # 点击退出账号button
        SettingsPageLogin.settings_page_popus_quit_login_but.click()

        logger.info("点击设置页退出账号，测试退出登录单账号场景")
        self.setUp()
        SettingsPageLogin.settings_page_quit_login_but.click()  # 点击退出账号button
        SettingsPageLogin.settings_page_popus_cancel_but.click()  # 取消弹窗
        SettingsPageLogin.settings_page_quit_login_but.click()
        SettingsPageLogin.settings_page_popus_append_account_but.click()
        LoginUtil.nebula_initial_page_login_account('15201889524', 'shi123456789')
        self.assert_equal('测试退出登录成功', SettingsPageLogin.switch_acount_page_title.exist(), False)
