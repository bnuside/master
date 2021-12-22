import os
import time
from krunner.utils import logger
from krunner.utils import adb
from krunner.utils import get_local_package_path
from krunner.conf import get_config_value
from krunner.plugins.login import LoginTool

from pageobjects.android.settings import Settings
from pageobjects.android.about_us import AboutUs
from conf.channels import get_channel
from testcase.krunner import KRunner
from conf.basic_info import *


class TestOEMChannelProtection(KRunner):
    """渠道号防覆盖测试"""

    @KRunner.post_setup
    def setUp(self):
        self.login_tool = LoginTool()
        if not self.login_tool.check_login():
            self.login_tool.login(code='+86', phone_num='13401046071', password='kuai0000')

    @KRunner.post_teardown
    def tearDown(self):
        self.driver.stop_app()

    def test_new_install(self):
        brand = adb.get_device_brand(sn)
        logger.debug(f'brand={brand}')
        self.driver.open_schema(scheme.settings)
        time.sleep(5)
        retry_count = 5
        while retry_count > 0 and not Settings.about_us.exist(1):
            self.driver.swipe_up()
            time.sleep(1)
            retry_count -= 1
        Settings.about_us.click()
        time.sleep(5)
        version_view = AboutUs.version
        assert version_view.exist(2)
        x = (version_view.info['bounds']['left'] + version_view.info['bounds']['right']) // 2
        y = (version_view.info['bounds']['top'] + version_view.info['bounds']['bottom']) // 2
        cmd = f"adb -s {sn} shell input tap {x} {y}"
        for i in range(8):
            os.popen(cmd)
            time.sleep(0.1)
        time.sleep(2)
        target = AboutUs.channel.find_element().get_text()
        logger.debug(f'target={target}')
        logger.debug(f'exp={get_channel(brand)}')
        self.assert_equal(f'预期渠道号是：[{get_channel(brand)}]，实际渠道号是：[{target}]', target, get_channel(brand))

    def test_re_install_instant(self):
        adb.clear_app_data(sn, pkg)
        time.sleep(5)
        re_apk_path = get_local_package_path(re_apk_url)
        adb.install_app(sn, re_apk_path)
        time.sleep(60)

        brand = adb.get_device_brand(sn)
        logger.debug(brand)
        logger.debug(get_channel(brand))
        self.driver.open_schema(scheme.settings)
        time.sleep(5)
        retry_count = 5
        while retry_count > 0 and not Settings.about_us.exist(1):
            self.driver.swipe_up()
            time.sleep(1)
            retry_count -= 1
        Settings.about_us.click()
        time.sleep(5)
        version_view = AboutUs.version
        assert version_view.exist(2)
        x = (version_view.info['bounds']['left'] + version_view.info['bounds']['right']) // 2
        y = (version_view.info['bounds']['top'] + version_view.info['bounds']['bottom']) // 2
        cmd = f"adb -s {sn} shell input tap {x} {y}"
        for i in range(8):
            os.popen(cmd)
            time.sleep(0.1)
        time.sleep(2)
        target = AboutUs.channel.find_element().get_text()
        logger.debug(f'target={target}')
        logger.debug(f'exp={get_channel(brand)}')
        self.assert_equal(f'预期渠道号是：[{get_channel(brand)}]，实际渠道号是：[{target}]', target, get_channel(brand))