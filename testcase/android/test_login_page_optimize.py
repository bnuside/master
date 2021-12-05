import os
import time

from pageobjects.android.login_optimize_page import LoginOptimizePage
from krunner.utils import logger
from krunner.utils import adb
from krunner.conf import get_config_value
from testcase.krunner import KRunner
from utils.login_util import LoginUtil


class TestLoginOptimize(KRunner):
    """快手登录优化测试"""

    def setUp(self):
        self.start_time = time.time()
        adb.clear_app_data(get_config_value('serialno')[0], get_config_value('pkg_name'))
        time.sleep(2)
        logger.info('启动快手')
        adb.start_schema(get_config_value('serialno')[0], get_config_value('kuaishou_schema')[0])
        time.sleep(2)
        self.driver.watch_alert()
        time.sleep(5)
        logger.info("杀死进程")
        os.popen(f'adb shell am force-stop {get_config_value("pkg_name")}')
        time.sleep(5)
        logger.info("进到手机号登录页面")
        adb.start_schema(get_config_value('serialno')[0], get_config_value('kuaishou_schema')[1])
        time.sleep(8)
        self.driver.watch_alert()
        logger.info("点击手机号登录")
        LoginOptimizePage.phone_login_but.click()
        time.sleep(2)

    def test_mobile_get_code_optimize(self):
        logger.info("测试获取验证码是否强化")
        self.assert_equal('测试获取验证码强化存在', LoginOptimizePage.get_mobilephone_code.exist(2), True)

    def test_email_login_optimize(self):
        logger.info("测试邮箱登录是否强化")
        LoginOptimizePage.smile_email_icon.click()
        time.sleep(2)
        self.assert_equal('测试邮箱登录强化存在', LoginOptimizePage.smile_microblog_icon.exist(2), True)

    def test_mobile_click_get_code(self):
        logger.info("测试手机号登录页面获取验证码点击")
        time.sleep(2)
        LoginUtil.operation_input_phone(self)
        logger.info("点击获取验证码")
        LoginOptimizePage.get_mobilephone_code.click()
        self.assert_equal('测试登录按钮存在', LoginOptimizePage.login_button.exist(2), True)
        time.sleep(60)
        logger.info("点击重新发送")
        LoginOptimizePage.retry_send_code.click()
        logger.info("断言重新发送不存在")
        self.assert_equal('测试重新发送不存在', not LoginOptimizePage.retry_send_code.exist(2), True)

    def test_mobile_keyboard_show_and_vanish(self):
        logger.info("测试手机号登录页面键盘的展示和消失")
        self.assert_equal('测试键盘存在', LoginOptimizePage.number_input_keyboard.exist(2), True)
        self.driver.back()  # 点击back按钮
        time.sleep(2)
        logger.info("断言键盘不存在")
        self.assert_equal('测试键盘不存在', not LoginOptimizePage.number_input_keyboard.exist(2), True)

    def test_email_keyboard_show_and_vanish(self):
        logger.info("测试邮箱登录页面键盘的展示和消失")
        LoginOptimizePage.smile_email_icon.click()
        time.sleep(2)
        self.assert_equal('测试键盘存在', LoginOptimizePage.email_input_keyboard.exist(2), True)
        self.driver.back()  # 点击back按钮
        time.sleep(2)
        logger.info("断言键盘不存在")
        self.assert_equal('测试键盘不存在', not LoginOptimizePage.email_input_keyboard.exist(2), True)
