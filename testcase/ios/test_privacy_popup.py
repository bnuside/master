#!/usr/bin/env python3
import time
from krunner.utils import logger
from krunner.conf import get_config_value
from pageobjects.ios.privacy_popup import PrivacyPopup
from testcase.krunner import KRunner


class TestPrivacyPopup(KRunner):
    """隐私弹窗测试"""

    @KRunner.post_setup
    def setUp(self):
        # self.start_time = time.time()
        self.driver.handle_alert('nothing')
        self.driver.uninstall(get_config_value('pkg_name'))
        time.sleep(5)
        self.driver.install_app()
        time.sleep(5)
        self.driver.start_app()
        time.sleep(5)

    def test_agree(self):
        """测试同意按钮"""
        logger.info('测试隐私弹窗上的同意按钮')
        time.sleep(10)
        assert PrivacyPopup.agree_button.exist(5)
        PrivacyPopup.agree_button.click()
        time.sleep(2)
        assert not PrivacyPopup.agree_button.exist()

    def test_disagree_and_enter_visitor(self):
        """测试不同意，进入访客模式按钮"""
        logger.info('测试隐私弹窗上的「不同意，并进入访客模式」按钮（9.11.10 版本推全）')
        time.sleep(10)
        assert PrivacyPopup.disagree_button.exist(5)
        PrivacyPopup.disagree_button.click()
        time.sleep(2)
        assert not PrivacyPopup.agree_button.exist()