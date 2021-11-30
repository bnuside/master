"""
@author:sunping
@time:2021/11/26:7:48 下午
"""
import sys
import time,os,uuid
from krunner.utils import logger
from krunner.utils import adb
from krunner.conf import get_config_value
from pageobjects.android.privacy_popup import PrivacyPopup
from pageobjects.android.kgi_popup import KgiPopup
from testcase.krunner import KRunner
from krunner.plugins.mock import Mock
from krunner.plugins.login import LoginTool
from testcase.android.abtest import addOrDeleteAbtest
class TestKgiPopup(KRunner):
    def start_app(self):
        adb.start_schema(get_config_value('serialno')[0], get_config_value('kuaishou_schema')[0])
        time.sleep(5)
    def test_kgi_01rdid(self):
        #self.driver.uninstall_app()
        random_did='ANDROID_' + str(uuid.uuid4()).replace('-', '')[:16]
        with open('testcase/android/uid_file' ,'w', encoding='utf-8') as f:
            f.write(random_did)
        adb.push_file(get_config_value('serialno')[0],'testcase/android/uid_file','/storage/emulated/0/Android/data/com.smile.gifmaker/cache/.t_did')
        addOrDeleteAbtest('add','mille_mobile_did_12','personalizedFeature','exp1',random_did,'1686505027')
        #self.driver.install_app(mode='unload', pkg_name='com.smile.gifmaker', password='ks123456') # 安装app
        # mode的overwrite为覆盖安装（默认），unload为卸载重装；pkg_name默认为配置的bundleid；password为OPPO和vivo用户提供安装输入密码功能
        #time.sleep(20)

    def test_kgi_02interest(self):

        self.start_app()
        time.sleep(3)
        self.driver.stop_app()
        time.sleep(3)
        self.start_app()
        self.driver.watch_alert()
        while True:
            self.driver.swipe_up()
            time.sleep(2)
            try:
                self.assert_equal('展示了兴趣标签弹窗',KgiPopup.kgi_interest_btn.exist(),True)
                logger.info("点击游戏选项")
                KgiPopup.kgi_interest_game_btn.click()
                logger.info("点击音乐选项")
                KgiPopup.kgi_interest_music_btn.click()
                self.assert_equal('提交按钮的展示', KgiPopup.kgi_interest_ok_btn.exist(), True)
                logger.info("点击提交按钮")
                KgiPopup.kgi_interest_submit_btn.click()
                self.assert_equal('提交兴趣标签展示toast', KgiPopup.kgi_interest_toast.exist(), True)
                break
            except Exception as e:
                logger.warning(e)

    def test_kgi_03follow(self):
         self.start_app()
         self.driver.watch_alert()
         while True:
            self.driver.swipe_up()
            time.sleep(2)
            try:
                self.assert_equal('关注引导弹窗展示', KgiPopup.kgi_follow_btn.exist(), True)
                self.assert_equal('去看看按钮展示',KgiPopup.kgi_follow_see.exist(),True)
                self.assert_equal('稍后再说按钮展示',KgiPopup.kgi_follow_later.exist(),True)
                KgiPopup.kgi_follow_see.click()
                self.assert_equal('跳转到大家都在看页面',KgiPopup.kgi_follow_allsee.exist(),True)
                time.sleep(2)
                self.driver.back()
                break
            except Exception as e:
                logger.warning(e)

    def test_kgi_04hot(self):
        self.start_app()
        self.driver.watch_alert()
        while True:
            self.driver.swipe_up()
            time.sleep(2)
            try:
                self.assert_equal('展示热榜引导',KgiPopup.kgi_hot_show.exist(),True)
                logger.info('点击搜索按钮')
                KgiPopup.kgi_search_btn.click()
                logger.info('跳转到热榜详情页')
                self.assert_equal('跳转到热榜详情页',KgiPopup.kgi_search_result.exist(),True)
                self.assert_equal('跳转到热榜详情页',KgiPopup.kgi_search_find.exist(),True)
                logger.info('点击返回到首页')
                self.driver.back()
                time.sleep(2)
                break
            except Exception as e:
                logger.warning(e)




















