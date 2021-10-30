#!/usr/bin/env python3
import time
from krunner.utils import logger
from krunner.conf import get_config_value
from pageobjects.ios.privacy_popup import PrivacyPopup
from testcase.krunner import KRunner


class TestPrivacyPopup(KRunner):
    """隐私弹窗测试"""

    def setUp(self):
        self.driver.uninstall(get_config_value('pkg_name'))
        time.sleep(5)
        self.driver.install_app()
        time.sleep(5)
        self.driver.start_app()
        time.sleep(5)

    def test_popup_three_pages(self):
        """能否弹出隐私弹窗"""

        logger.info("等待启动完成，闪屏加载完成")
        time.sleep(5)
        assert PrivacyPopup.agree_button.exist(5)
        assert PrivacyPopup.disagree_button.exist(5)
        #
        PrivacyPopup.disagree_button.click()
        time.sleep(2)
        #
        assert PrivacyPopup.agree_button.exist(5)
        assert PrivacyPopup.check_policy_button.exist(5)
        assert PrivacyPopup.disagree_again_button.exist(5)

        PrivacyPopup.disagree_again_button.click()
        time.sleep(2)

        assert PrivacyPopup.agree_button.exist(5)
        assert PrivacyPopup.check_policy_button.exist(5)
        assert PrivacyPopup.enter_visitor_model_button.exist(5) or PrivacyPopup.exit_button.exist(5)

        PrivacyPopup.check_policy_button.click(5)
        time.sleep(2)

        assert PrivacyPopup.agree_button.exist(5)
        assert PrivacyPopup.disagree_button.exist(5)

        PrivacyPopup.agree_button.click()

    def test_popup_p1_agree(self):
        time.sleep(5)
        PrivacyPopup.agree_button.click(5)
        assert not PrivacyPopup.agree_button.exist(5)

    def test_popup_p2_agree(self):
        time.sleep(5)
        PrivacyPopup.disagree_button.click(5)
        time.sleep(2)

        PrivacyPopup.agree_button.click(5)
        assert not PrivacyPopup.agree_button.exist(5)

    def test_popup_p3_agree(self):
        time.sleep(5)
        PrivacyPopup.disagree_button.click(5)
        time.sleep(2)

        PrivacyPopup.disagree_again_button.click(5)
        time.sleep(2)

        PrivacyPopup.agree_button.click(5)
        assert not PrivacyPopup.agree_button.exist(5)