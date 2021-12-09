import os
import time

from krunner.utils import logger
from krunner.utils import adb
from krunner.conf import get_config_value

from pageobjects.android.login_optimize_page import LoginOptimizePage
from pageobjects.android.main_page import MainPage
from testcase.krunner import KRunner
from utils.login_util import LoginUtil


class TestLoginOptimize(KRunner):
    """快手登录优化测试"""

    @KRunner.post_setup
    def setUp(self):
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
        logger.info("进到主页面")
        adb.start_schema(get_config_value('serialno')[0], get_config_value('kuaishou_schema')[0])
        time.sleep(10)
        self.driver.watch_alert()
        time.sleep(2)

    def test_login_but_function_and_show(self):
        self.assert_equal('测试强化后的按钮存在', MainPage.intensified_login_but.exist(2), True)

        logger.info('点击发现')
        MainPage.btn_find.click(2)
        self.assert_equal('测试强化后的按钮不存在', MainPage.intensified_login_but.exist(2), False)

        logger.info('点击搜索')
        MainPage.smile_btn_search.click(3)
        if MainPage.search_find_title.exist(3):
            time.sleep(5)
            self.assert_equal('测试搜索发现存在', MainPage.search_find_title.exist(3), True)
        else:
            logger.error("搜索功能无法使用")
        MainPage.smile_search_page_back_but.click(3)
        time.sleep(3)

        MainPage.btn_jingxuan.click_if_exist(3)
        time.sleep(2)
        MainPage.intensified_login_but.click()  # 强化按钮的点击
        time.sleep(3)
        logger.info("点击手机号登录")
        LoginOptimizePage.phone_login_but.click()
        time.sleep(2)
        LoginUtil.smile_initial_page_login_phone_account('17316287580', 'shi123456789', 2)
        self.assert_equal('测试登录完成，且强化按钮不存在', MainPage.intensified_login_but.exist(3), False)
