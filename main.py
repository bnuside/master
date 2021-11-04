#!/usr/bin/env python3
import click
from krunner.conf import update_config_value
from krunner.utils import logger
from krunner import __version__
from krunner.utils.errors import ParamsError
from testcase import TestSuiteBase

logo = """
    __ __ ____
   / //_// __ \__  ______  ____  ___  _____
  / ,<  / /_/ / / / / __ \/ __ \/ _ \/ ___/
 / /| |/ _, _/ /_/ / / / / / / /  __/ /
/_/ |_/_/ |_|\__,_/_/ /_/_/ /_/\___/_/ """

logger.info(f"{logo}  {__version__} \n")


@click.command()
@click.option('-t', '--test_type', default='', type=click.Choice(['android', 'ios']), help='test type, android/ios')
@click.option('-n', '--pkg_name', default='', type=str, help='package_name for android; bundleid for ios')
@click.option('-p', '--pkg_path', default='', type=str, help='package_download_url or local_package_path')
@click.option('-s', '--serialno', type=str, multiple=True, help='the android device serial number or ios device udid')
@click.option('-H', '--host', default='127.0.0.1', type=str,
              help='the android remote adb server host, [default=127.0.0.1]')
@click.option('-P', '--port', default=5037, type=int, help='the android remote adb server port, [default=5037]')
@click.option('-w', '--wda_path', default='', type=str, help='wda xcode project path')
@click.option('--wda_proxy_url', default='', type=str, help='the wda iproxy url, used it to connect wda server')
@click.option('--test_package', type=str, multiple=True,
              help='run tests from test_package, eg: --test_package testcase.ios')
@click.option('--test_module', type=str, multiple=True,
              help='run tests from test_module, eg: --test_module testcase.ios.test_demo')
@click.option('--test_class', type=str, multiple=True,
              help='run tests from module.TestClass, eg: --test_class testcase.ios.test_demo.TestDemo')
@click.option('--test_method', type=str, multiple=True,
              help='run specified test method, eg: --test_method testcase.ios.test_demo.TestDemo.test_example')
@click.option('--run_times', type=int, default=1, help='testcases execute times')
@click.option('--install/--no-install', default=False, help='need to reinstall the app')
@click.option('--execute_id', type=int, help='the task execute id')
@click.option('--home_scheme', type=str, help='home page scheme')
def main(test_type, pkg_name, pkg_path, serialno, install, host, port, wda_path, wda_proxy_url,
         test_package, test_module, test_class, test_method, run_times, execute_id, home_scheme):
    if not test_type:
        raise ParamsError('the param: test_type must be set, usage: --test_type xxx')
    if not pkg_name:
        raise ParamsError('the param: pkg_name must be set, usage: --pkg_name xxx')
    if install and not pkg_path:
        raise ParamsError('if you set install , you must set pkg_path, usage: --pkg_path xxx --install')
    if not serialno:
        raise ParamsError('the param: serialno must be set, usage: -s xxx')
    if not test_package and not test_module and not test_class and not test_method:
        raise ParamsError(f'one of the params: test_package or test_module or test_class or test_method must be set')

    update_config_value('test_type', value=test_type)
    update_config_value('pkg_name', value=pkg_name)
    update_config_value('pkg_path', value=pkg_path)
    update_config_value('serialno', value=list(serialno))
    update_config_value('android', 'adb_server_host', value=host)
    update_config_value('android', 'adb_server_port', value=port)
    update_config_value('ios', 'wda_path', value=wda_path)
    update_config_value('ios', 'wda_proxy_url', value=wda_proxy_url)
    update_config_value('ios', 'need_launch_wda', value=False) if wda_proxy_url else update_config_value('ios',
                                                                                                         'need_launch_wda',
                                                                                                         value=True)
    update_config_value('execute_id', value=execute_id)
    update_config_value('home_scheme', value=home_scheme)

    testsuite = TestSuiteBase(test_package=list(test_package), test_module=list(test_module),
                              test_class=list(test_class),
                              test_method=list(test_method), run_times=run_times, install=install)
    testsuite.run_test()


if __name__ == '__main__':
    main()
