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

    def setUp(self):
        # adb.clear_app_data(get_config_value('serialno')[0], get_config_value('pkg_name'))
        # time.sleep(5)
        get_config_value
        adb.start_schema(get_config_value('serialno')[0], get_config_value('home_scheme'))
        time.sleep(5)


    def test_interest_tag(self):
        """兴趣标签"""
        # logger.info("等待启动完成，闪屏加载完成")
        self.driver.watch_alert()

        """兴趣标签展示"""

        self.mock = Mock(host='kproxy.host',port=4947,token='200021_6e5bb5167343cc7763db061a92a265ea',user='sunping')
        self.mock.start_rule(3555) # mockid
        self.mock.set_proxy() # android通过adb设置全局代理 ios通过启动app的环境参数实现代理
        # your code
        # for i in range(4):
        #     self.driver.swipe_up()
        self.driver.back()
        assert InterestPopup.interest_btn.exist(3)
        InterestPopup.interest_game_btn.click()
        InterestPopup.interest_music_btn.click()
        InterestPopup.interest_submit_btn.click()
        time.sleep(2)
        self.mock.stop_rule(3555)
        self.mock.del_proxy()

















