#!/usr/bin/env python3
import traceback

from krunner.runner import Runner
from krunner.utils import logger


class KRunner(Runner):
    """你可以根据业务需求定制化你的KRunner类
可以重写setUp, tearDown方法, 没有特殊需求不用重写"""

    def __init__(self, test_method):
        super(KRunner, self).__init__(test_method)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # do something

    @classmethod
    def tearDownClass(cls):
        # do something
        super().tearDownClass()

    @Runner.post_setup
    def setUp(self):
        self.driver.force_start_app()
        # do something

    @Runner.post_teardown
    def tearDown(self):
        # do something
        pass

    def local_setup(func):
        def wrapper(self, *args):
            logger.info('=====local setup')
            # do something
            func(self, *args)

        return wrapper

    def local_teardown(func):
        def wrapper(self, *args):
            logger.info('=====local teardown')
            func(self, *args)
            # do something

        return wrapper