# -*- coding: utf-8 -*- 
# @Author  :zhujungui
# @Time    :2021/11/3 20:42
# @File    :open_setting_push
import time
from krunner.core.android.element import AndroidElement



class OpenSettingPush(object):

    '''不同手机开启通知元素定位'''

    # OPPO手机定位元素
    application_Btn=AndroidElement(xpath='//*[@text="应用管理"]',annotation='设置页应用管理按钮')
    application_list=AndroidElement(xpath='//*[@text="应用列表"]',annotation='应用列表')
    kuaishou_application=AndroidElement(xpath='//*[@text="快手"]',annotation='快手应用')
    logo=AndroidElement(xpath='//*[@text="快手"]',annotation='快手logo')
    application_push=AndroidElement(xpath='//*[@text="应用信息"]',annotation='应用信息按钮')
    push_notification=AndroidElement(xpath='//*[@text="通知管理"]',annotation='通知管理')
    alow_push=AndroidElement(xpath='//*[@text="允许通知"]',annotation='允许通知')

