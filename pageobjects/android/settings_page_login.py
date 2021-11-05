import os

from krunner.core.android.element import AndroidElement
from krunner.core.base import ImgElement


class SettingsPageLogin(object):
    """极速版设置页登录相关元素"""
    curr_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'template')

    phone_login_but = AndroidElement(text='手机号登录', annotation='手机号登录')
    settings_page_switch_account_but = AndroidElement(text='切换帐号', annotation='切换帐号')
    nebula_switch_acount_page_append_account_but = AndroidElement(
        xpath='//*[@resource-id="com.kuaishou.nebula:id/side_account_avatar"]',
        annotation='切换帐号')
    settings_page_quit_login_but = AndroidElement(text='退出登录', annotation='设置页退出登录')
    settings_page_popus_append_account_but = AndroidElement(text='添加新帐号', annotation='设置页弹窗的添加新帐号')
    settings_page_popus_quit_login_but = AndroidElement(text='退出登录', annotation='设置页弹窗的退出登录')
    settings_page_popus_cancel_but = AndroidElement(text='取消', annotation='设置页弹窗的取消')
    settings_page_popus_change_acount_but = AndroidElement(text='换个账号登录', annotation='设置页弹窗的换个账号登录')
    nebula_switch_acount_page_change_acount_first_but = AndroidElement(
        xpath='//*[@resource-id="com.kuaishou.nebula:id/main_account_avatar"]', annotation='切换第一个账号头像')
    nebula_switch_acount_page_change_acount_second_but = AndroidElement(
        xpath='//*[@resource-id="com.kuaishou.nebula:id/side_account_avatar"]', annotation='切换第二个账号头像')
    switch_acount_page_popus_quit_but = AndroidElement(text='退出', annotation='切换账号页面弹窗的退出')
    switch_acount_page_popus_cancel_but = AndroidElement(text='取消', annotation='取消')
    switch_acount_page_title = AndroidElement(text='轻触头像以切换帐号'
                                              , annotation='轻触头像以切换帐号')
    initial_page_phone_input = AndroidElement(text='请输入手机号', annotation='输入手机号')
    initial_page_switch_pwd_login = AndroidElement(text='密码登录', annotation='密码登录切换')
    nebula_initial_page_pwd_input = AndroidElement(
        xpath='//*[@resource-id="com.kuaishou.nebula:id/user_phone_num_info"]',
        annotation='密码输入框')
    nebula_initial_page_privacy_agree = AndroidElement(
        xpath='//*[@resource-id="com.kuaishou.nebula:id/protocol_checkbox"]',
        annotation='同意隐私文案')
    initial_page_login_but = AndroidElement(text='登录', annotation='登录')
    nebula_first_account_photo = AndroidElement(xpath='//*[@resource-id="com.kuaishou.nebula:id/icon_one"]',
                                                annotation='登录页面第一个头像')
    nebula_second_account_photo = AndroidElement(xpath='//*[@resource-id="com.kuaishou.nebula:id/icon_two"]',
                                                 annotation='登录页面第二个头像')
