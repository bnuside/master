import os

from krunner.core.android.element import AndroidElement
from krunner.core.base import ImgElement


class SettingsPageLogin(object):
    """设置页登录相关元素"""

    curr_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'template')

    phone_login_but = AndroidElement(text='手机号登录', annotation='手机号登录')
    settings_page_switch_account_but = AndroidElement(text='切换帐号', annotation='切换帐号')
    switch_acount_page_append_account_but = AndroidElement(
        xpath='//*[@resource-id="com.kuaishou.nebula:id/side_account_avatar"]',
        annotation='切换帐号')
    settings_page_quit_login_but = AndroidElement(text='退出登录', annotation='设置页退出登录')
    settings_page_popus_append_account_but = AndroidElement(text='添加新帐号', annotation='设置页弹窗的添加新帐号')
    settings_page_popus_quit_login_but = AndroidElement(text='退出登录', annotation='设置页弹窗的退出登录')
    settings_page_popus_cancel_but = AndroidElement(text='取消', annotation='设置页弹窗的取消')
    settings_page_popus_change_acount_but = AndroidElement(text='换个账号登录', annotation='设置页弹窗的换个账号登录')
    switch_acount_page_change_acount_first_but = AndroidElement(
        xpath='//*[@resource-id="com.kuaishou.nebula:id/main_account_avatar"]', annotation='切换第一个账号头像')
    switch_acount_page_change_acount_second_but = AndroidElement(
        xpath='//*[@resource-id="com.kuaishou.nebula:id/side_account_avatar"]', annotation='切换第二个账号头像')
    switch_acount_page_popus_quit_but = AndroidElement(text='退出', annotation='切换账号页面弹窗的退出')
    switch_acount_page_popus_cancel_but = AndroidElement(text='取消', annotation='取消')
    switch_acount_page_title = AndroidElement(text='轻触头像以切换帐号'
                                              , annotation='轻触头像以切换帐号')