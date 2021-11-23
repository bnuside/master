#! /usr/bin/python3
import time

from krunner.utils import logger
from krunner.utils import adb
from krunner.plugins.login import LoginTool
from krunner.conf import get_config_value
from krunner.core.android.element import AndroidElement
from pageobjects.android.growth_cleaner import GrowthCleaner
from pageobjects.android.rank_page import RankPage
from pageobjects.android.selection_page import SelectionPage
from testcase.krunner import KRunner


class TestGrowthCleaner(KRunner):
    """主站垃圾清理功能测试"""

    def test_clean_entry_show(self):
        logger.info("长按 icon 展示垃圾待清理入口")
        adb.start_schema(get_config_value('serialno')[0], 'kwai://home')
        self.driver.watch_alert()
        time.sleep(20)
        self.driver.go_home()
        AndroidElement(description='快手', annotation='快手icon').long_click()
        time.sleep(3)
        self.assert_equal("垃圾待清理入口已经展示", GrowthCleaner.entry.exist(), True)

    def test_clean_garbage(self):
        logger.info("进入垃圾清理页面,扫描垃圾，清理并跳转至垃圾清理完成页面")
        self.driver.go_home()
        AndroidElement(description='快手', annotation='快手icon').long_click()
        logger.info("点击入口进入垃圾清理页面")
        GrowthCleaner.entry.click_if_exist()
        time.sleep(3)
        logger.info("开始扫描垃圾")
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

    def test_rank_click(self):
        self.test_clean_garbage()
        logger.info("点击清理完成页面的'今日热'按钮")
        GrowthCleaner.hot_rank_btn.click()
        self.assert_equal('成功进入热榜页面', RankPage.rank_tab.exist(), True)

    def test_selection_btn_click(self):
        self.test_clean_garbage()
        logger.info("点击清理完成页面的'刷精选'按钮")
        GrowthCleaner.selection_btn.click()
        self.assert_equal('成功进入精选页面', SelectionPage.like_btn.exist(), True)


