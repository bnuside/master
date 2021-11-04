import importlib
import inspect
import json
import os
import re
import time
import traceback
import typing
import unittest
from modulefinder import ModuleFinder

from krunner.core.android.driver import AndroidDriver
from krunner.core.ios.driver import IosDriver
from krunner.runner import Runner
from krunner.utils.report import HTMLTestRunner
from krunner.utils import (
    logger,
    remove_local_package,
    upload_files_kcdn,
    httpdo, file)
from krunner.conf import (
    TEST_RESULT_DIR,
    get_config_value,
    write_json_config,
    result_template,
    TestCaseResultCode)

from conf import ATTM_URL


def parametrize(testcase_clazz):
    """
    Used for passed parameters for test case instance.
    :param testcase_clazz:
    :return: test suite for given test case class
    """
    test_loader = unittest.TestLoader()
    testcase_names = test_loader.getTestCaseNames(testcase_clazz)
    suite = unittest.TestSuite()
    for testcase_name in testcase_names:
        suite.addTest(testcase_clazz(testcase_name))
    return suite


def get_test_module_path(test_module):
    path = os.getcwd()
    packages = test_module.split('.')
    for package in packages:
        path = os.path.join(path, package)
    test_module_path = os.path.join(f"{path}.py")
    if not os.path.isfile(test_module_path):
        from krunner.utils import logger
        logger.warning(f"Skipped, module: {test_module} not exists")
        return None
    return test_module_path


def get_import_module_classes(module_path):
    """
    :param module_path: str
        eg. /Users/xxx/tmp/krunner-demo/testcase/ios/test_demo2.py
    :return: dict
        {
            'DirEntry': <class 'posix.DirEntry'>,
            'GenericAlias': <class 'types.GenericAlias'>,
            'Mapping': <class 'collections.abc.Mapping'>,
            'MutableMapping': <class 'collections.abc.MutableMapping'>,
            'IosDriver': <class 'krunner.core.ios.driver.IosDriver'>,
            ...
            'OcrDetector': <class 'detector.core.ocr.OcrDetector'>
        }

    """
    classes_dict = {}
    m_finder = ModuleFinder(path=[])
    m_finder.run_script(module_path)
    exclude_module_names = m_finder.badmodules.keys()
    for exclude_module_name in exclude_module_names:
        exclude_module_info = importlib.import_module(exclude_module_name)
        for name, obj in inspect.getmembers(exclude_module_info, inspect.isclass):
            classes_dict[name] = obj
    return classes_dict


def get_all_classees_under_module(test_module):
    """
    :param test_module: testcase.ios.test_demo_1
    :return: dict
        {
            'KRunner': <class 'testcase.krunner.KRunner'>,
            'TestDemo': <class 'testcase.ios.test_demo.TestDemo'>,
            'TestDemo2': <class 'testcase.ios.test_demo.TestDemo2'>
        }
    """
    classes_dict = {}
    module_info = importlib.import_module(test_module)
    for name, obj in inspect.getmembers(module_info, inspect.isclass):
        classes_dict[name] = obj
    return classes_dict


def get_test_clazz_dict(test_module):
    """
    :param test_module: testcase.ios.test_demo_1
    :return:  dict
        {'TestDemo': <class 'testcase.ios.test_demo.TestDemo'>,
        'TestDemo2': <class 'testcase.ios.test_demo_2.TestDemo2'>,
        'TestDemo3': <class 'testcase.ios.test_demo_3.TestDemo3'>}
    """
    test_clazz_dict = {}
    test_module_path = get_test_module_path(test_module)
    logger.debug(f"module_path: {test_module_path}")
    if test_module_path:
        classes_dict = get_all_classees_under_module(test_module)
        all_exclude_classes_dict = {}
        exclude_classes_dict = get_import_module_classes(test_module_path)
        all_exclude_classes_dict = {**all_exclude_classes_dict, **exclude_classes_dict}

        exclude_class_keys = set(all_exclude_classes_dict.keys())
        classes_keys = set(classes_dict.keys())
        test_clazz_names = list(classes_keys - exclude_class_keys)
        for clazz_name in test_clazz_names:
            test_clazz_dict[clazz_name] = classes_dict.get(clazz_name)
        test_clazz_list = sorted(test_clazz_dict.items(),
                                 key=lambda item: item[0],
                                 reverse=False)
        # print('test_clazz_list:{}'.format(test_clazz_list))
        test_clazz_dict = {}
        for test_clazz in test_clazz_list:
            for i in range(len(test_clazz)):
                test_clazz_dict[test_clazz[0]] = test_clazz[1]
        # print('test_clazz_dict:{}'.format(test_clazz_dict))
        return test_clazz_dict
    return None


def get_file_names(dst, prefix=''):
    files = []
    for (dirpath, dirnames, names) in os.walk(dst):
        for name in names:
            if name.startswith(prefix) and "__pycache__" not in dirpath:
                files += [os.path.join(dirpath, name)]
    return files


def get_test_modules_under_package(package: str) -> list:
    """
    :param package:  eg. 'testcase.ios'
    :return: list
        ['testcase.ios.test_demo', 'testcase.ios.test_demo_2']
    """
    test_modules = []
    base_dir = os.getcwd()
    for p in package.split("."):
        base_dir = os.path.join(base_dir, p)
    files = get_file_names(base_dir)
    if files:
        for file in files:
            raw = file.replace("/", ".").replace("\\", ".")
            module = "".join(["testcase", raw.split("testcase")[-1].rsplit(".", 1)[0]])
            test_modules.append(module)
    return test_modules


def get_test_methods(test_class):
    """
    :param test_class: testcase.ios.test_demo.TestDemo
    :return:
        ['testcase.ios.test_demo.TestDemo.test_create_video',
        'testcase.ios.test_demo.TestDemo.test_create_video_2']
    """
    test_methods = []
    test_module = test_class.rsplit('.', 1)[0]
    tmp_methods = []
    for key, clazz_obj in get_test_clazz_dict(test_module).items():
        test_loader = unittest.TestLoader()
        tmp_methods.extend(test_loader.getTestCaseNames(clazz_obj))
    for tmp_method in tmp_methods:
        test_methods.append("".join([test_class, ".", tmp_method]))
    return test_methods


class TestSuiteBase(object):
    def __init__(self, test_package=None, test_module=None, test_class=None,
                 test_method=None, run_times=1, install=False):

        self._test_package = test_package
        self._test_module = test_module
        self._test_class = test_class
        self._test_method = test_method
        self.run_times = run_times
        self.install = install
        self.start_time = int(time.time())

    def run_test(self):
        result_dir = f"{TEST_RESULT_DIR}/{os.environ.get('SINGLE_TEST_RESULT_DIR')}"
        logger.info(f"=====Test result dir: {result_dir}")
        driver: typing.Union[IosDriver, AndroidDriver] = Runner.get_driver()
        if self.install:
            driver.install_app(mode="overwrite")
        if isinstance(driver, AndroidDriver):
            flag = get_config_value("android", "alert_watcher")
            if flag or flag is None:
                driver.watch_alert()

        try:
            suite = self._gen_testsuite()
        except Exception as _:
            logger.error(traceback.format_exc())
            raise

        # unittest.TextTestRunner(verbosity=2).run(suite)
        with(open(f'{result_dir}/report.html', 'wb')) as fp:
            runner = HTMLTestRunner(
                stream=fp,
                verbosity=2,
                title='Test Report',
                description='describe: ...'
            )
            runner.run(suite)

        if isinstance(driver, AndroidDriver):
            driver.stop_watcher()

        remove_local_package()
        result_data = self._generate_result_data()
        write_json_config(f'{result_dir}/report.json', result_data)
        logger.debug('Result data:' + json.dumps(result_data, indent='  ', ensure_ascii=False))
        if get_config_value("need_upload_result"):
            logger.info('==================上报result到ATTM==================')
            url = f"{ATTM_URL}/attm/result/addResult"
            res = httpdo("post", url, json=result_data, headers={'content-type': 'application/json'})
            logger.info(f"Upload data to ATTM: {res}")
            # logger.info(f"Remove the testresult dir: {result_dir}")
            # file.remove_dir(result_dir)

    def _gen_testsuite(self):
        test_packages = self._convert(self._test_package)
        test_modules = self._convert(self._test_module)
        test_classes = self._convert(self._test_class)
        test_methods = self._convert(self._test_method)
        logger.info(f"test_packages: {test_packages}; test_modules: {test_modules}; "
                    f"test_classes: {test_classes}; test_methods: {test_methods}")

        test_suite = unittest.TestSuite()
        if test_packages:
            for package in test_packages:
                temp_modules = get_test_modules_under_package(package)
                test_modules.extend(temp_modules)

        if test_modules:
            for module in test_modules:
                test_class_dict = get_test_clazz_dict(module)
                if test_class_dict:
                    for key, clazz in test_class_dict.items():
                        test_suite.addTest(parametrize(clazz))
        if test_classes:
            for test_class in test_classes:
                test_class_dict = get_test_clazz_dict(test_class.rsplit(".", 1)[0])
                if test_class_dict:
                    flag = 0
                    for key, clazz in test_class_dict.items():
                        if key == test_class.rsplit(".", 1)[-1]:
                            test_suite.addTest(parametrize(clazz))
                            flag += 1
                    if not flag:
                        logger.warning(f"Skipped, The test_class: {test_class} does not exists")

        if test_methods:
            for test_method in test_methods:
                test_class_dict = get_test_clazz_dict(test_method.rsplit(".", 2)[0])
                if test_class_dict:
                    flag = 0
                    for key, clazz in test_class_dict.items():
                        tmp_methods = get_test_methods(str(re.findall(r"'(.+?)'", str(clazz))[0]))
                        if test_method in tmp_methods:
                            test_suite.addTest(clazz(test_method.rsplit(".", 1)[-1]))
                            flag += 1
                    if not flag:
                        logger.warning(f"Skipped, The test_method: {test_method} does not exists")

        return test_suite

    def _convert(self, raw_data: list):
        """
        :param raw_data: list
            ["test.ios.test_demo, test.ios.test_demo2", "test.ios.test_demo3", ""]
        :return: list
            ["test.ios.test_demo", "test.ios.test_demo2", "test.ios.test_demo3"]
        """
        raw_data = [x for x in raw_data if x != '']
        data = []
        for item in raw_data:
            data.extend([i.strip() for i in item.split(",")])
        final_data = []
        for i in range(self.run_times):
            final_data.extend(data)
        return final_data

    def _generate_result_data(self):
        result_template["bizType"] = 2
        result_template['type'] = 'krunner'
        result_template["execId"] = get_config_value("execute_id")
        if result_template["resultSummary"]['errors']:
            result_template["status"] = TestCaseResultCode.ERROR
        elif result_template["resultSummary"]['failures']:
            result_template["status"] = TestCaseResultCode.FAILURE
        elif result_template["resultSummary"]['passed']:
            result_template["status"] = TestCaseResultCode.PASSED
        else:
            result_template["status"] = TestCaseResultCode.ERROR
        result_template["resultSummary"]["platform"] = get_config_value("test_type")
        result_template["resultSummary"]["start_time"] = self.start_time
        result_template["resultSummary"]["duration"] = int(time.time()) - self.start_time
        eid = os.environ.get('SINGLE_TEST_RESULT_DIR')
        log_path = os.path.join("testresult", eid, f"{eid}.log")

        need_upload = get_config_value("need_upload_result")
        cdn_log_urls = upload_files_kcdn([log_path]) if need_upload else None
        result_template["resultSummary"]["log_url"] = cdn_log_urls[0] if cdn_log_urls else None
        return result_template