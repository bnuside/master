import time,os
from krunner.utils import logger
from krunner.utils import adb
from krunner.conf import get_config_value
from pageobjects.android.privacy_popup import PrivacyPopup
from pageobjects.android.interest_popup import InterestPopup
from testcase.krunner import KRunner
from krunner.plugins.mock import Mock

from krunner.plugins.login import LoginTool


class TestInterestPopup(KRunner):

    def start_app(self):
        adb.start_schema(get_config_value('serialno')[0], get_config_value('kuaishou_schema')[0])
        time.sleep(5)
    def interest_mock(self):
        self.mock = Mock(host='kproxy.host',port=4947,token='200021_6e5bb5167343cc7763db061a92a265ea',user='sunping')
        self.mock.start_rule(3555)
        self.mock.set_proxy()

    def test_interest_tag_page1(self):
        self.driver.watch_alert()
        self.interest_mock()
        self.driver.shell("am force-stop com.smile.gifmaker")
        time.sleep(3)
        self.start_app()
        logger.info("安卓back触发兴趣标签页展示")
        self.driver.back()
        logger.info("点击游戏按钮")
        InterestPopup.interest_game_btn.click()
        logger.info("点击音乐按钮")
        InterestPopup.interest_music_btn.click()
        logger.info("点击提交按钮")
        self.assert_equal('展示兴趣标签弹窗', InterestPopup.interest_submit_btn.exist(), True)
        InterestPopup.interest_submit_btn.click()
        self.assert_equal('提交兴趣标签', InterestPopup.interest_toast_btn.exist(), True)
        time.sleep(3)

    def test_interest_tag_page2(self):
        self.driver.watch_alert()
        self.interest_mock()
        logger.info("强制杀死进程")
        self.driver.shell("am force-stop com.smile.gifmaker")
        time.sleep(3)
        logger.info("重新启动app")
        self.start_app()
        logger.info("启动app成功")
        self.driver.back()
        logger.info("点击全部按钮")
        InterestPopup.interest_all_btn.click(3)
        logger.info("选择任意一个标签")
        InterestPopup.interest_any_btn.click()
        logger.info("点击提交")
        InterestPopup.interest_submit_btn.click(3)

        self.assert_equal('提交兴趣标签展示toast', InterestPopup.interest_toast_btn.exist(), True)


    def test_interest_tag_close(self):
        self.driver.watch_alert()
        self.interest_mock()
        self.driver.shell("am force-stop com.smile.gifmaker")
        time.sleep(3)
        self.start_app()
        time.sleep(3)
        self.driver.back()
        assert InterestPopup.interest_close_btn.exist(2)
        InterestPopup.interest_close_btn.click(3)


















