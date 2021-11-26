import time
from krunner.utils import logger
from krunner.utils import adb
from krunner.conf import get_config_value

from pageobjects.android.privacy_popup import PrivacyPopup
from testcase.krunner import KRunner


class TestPrivacyPopup(KRunner):
    """快手隐私弹窗测试"""

    def setUp(self):
        adb.clear_app_data(get_config_value('serialno')[0], get_config_value('pkg_name'))
        time.sleep(5)
        adb.start_schema(get_config_value('serialno')[0], get_config_value('home_scheme'))
        time.sleep(5)

    def test_popup_three_pages(self):
        """能否弹出隐私弹窗"""

        logger.info("等待启动完成，闪屏加载完成")
        time.sleep(20)
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
        time.sleep(20)
        PrivacyPopup.agree_button.click(5)
        assert not PrivacyPopup.agree_button.exist(5)

    def test_popup_p2_agree(self):
        time.sleep(20)
        PrivacyPopup.disagree_button.click(5)
        time.sleep(2)

        PrivacyPopup.agree_button.click(5)
        assert not PrivacyPopup.agree_button.exist(5)

    def test_popup_p3_agree(self):
        time.sleep(20)
        PrivacyPopup.disagree_button.click(5)
        time.sleep(2)

        PrivacyPopup.disagree_again_button.click(5)
        time.sleep(2)

        PrivacyPopup.agree_button.click(5)

        assert not PrivacyPopup.agree_button.exist(5)