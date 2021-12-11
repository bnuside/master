#! /usr/bin/python3
import time
from krunner.utils import logger
from krunner.utils import adb
from krunner.conf import get_config_value
from krunner.core.android.element import AndroidElement
from pageobjects.android.growth_cleaner import GrowthCleaner
from pageobjects.android.rank_page import RankPage
from pageobjects.android.selection_page import SelectionPage
from testcase.krunner import KRunner


class TestGrowthCleaner(KRunner):
    """主站垃圾清理功能测试"""

    @staticmethod
    def _enter_clean_page():
        #  kwai://cleaner
        logger.info("开始扫描垃圾")
        scheme = f'{TestGrowthCleaner._get_scheme_head()}cleaner'
        adb.start_schema(get_config_value('serialno')[0], scheme)
        time.sleep(30)

    @staticmethod
    def _enter_clean_end_page():
        #  先扫描一次
        TestGrowthCleaner._enter_clean_page()
        time.sleep(3)
        if GrowthCleaner.cleaner_selected_btn.exist():
            logger.info("点击清理垃圾按钮，进行垃圾清理")
            GrowthCleaner.cleaner_selected_btn.click()
            time.sleep(5)
        else:
            logger.info("未选中垃圾，直接点击完成按钮")
            GrowthCleaner.cleaner_not_selected_btn.click()

    @staticmethod
    def _get_scheme_head():
        pkg = get_config_value('pkg_name')
        return get_config_value('scheme_head')[pkg]

    @KRunner.post_teardown
    def tearDown(self):
        self.driver.back()
        time.sleep(1)

    def test_clean_entry_show(self):
        logger.info("长按 icon 展示垃圾待清理入口")
        adb.start_schema(get_config_value('serialno')[0], f'{self._get_scheme_head()}home')
        time.sleep(20)
        logger.info('显示手机桌面')
        self.driver.go_home()
        time.sleep(2)
        self.driver.swipe_up()
        logger.info('尝试长按桌面快手图标')
        AndroidElement(description='快手', annotation='快手icon').long_click()
        time.sleep(3)
        self.assert_equal("垃圾待清理入口已经展示", GrowthCleaner.clean_entry.exist(5), True)

    def test_clean_garbage(self):
        logger.info("进入垃圾清理页面,扫描垃圾，清理并跳转至垃圾清理完成页面")
        self._enter_clean_page()
        GrowthCleaner.scan_btn.click_if_exist()
        time.sleep(2)
        if GrowthCleaner.cleaner_selected_btn.exist():
            logger.info("点击清理垃圾按钮，进行垃圾清理")
            GrowthCleaner.cleaner_selected_btn.click()
            time.sleep(5)
        else:
            logger.info("未选中垃圾，直接点击完成按钮")
            GrowthCleaner.cleaner_not_selected_btn.click()
        self.assert_equal('进入清理完成页面，出现重新扫描按钮', GrowthCleaner.rescan_btn.exist(), True)

    def test_rescan_click(self):
        self._enter_clean_end_page()
        time.sleep(10)
        logger.info("点击清理完成页面的'重新扫描'按钮")
        GrowthCleaner.rescan_btn.click()

    def test_rank_click(self):
        self._enter_clean_end_page()
        time.sleep(10)
        logger.info("点击清理完成页面的'今日热'按钮")
        GrowthCleaner.hot_rank_btn.click()
        self.assert_equal('成功进入热榜页面', RankPage.rank_tab.exist(), True)

    def test_selection_btn_click(self):
        self._enter_clean_end_page()
        time.sleep(10)
        logger.info("点击清理完成页面的'刷精选'按钮")
        GrowthCleaner.selection_btn.click()
        self.assert_equal('成功进入精选页面', SelectionPage.like_btn.exist(), True)
