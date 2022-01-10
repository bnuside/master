# -*- coding: utf-8 -*-
# @Time    : 2021/10/01 19:32
# @Author  : Zhujungui
# @FileName: open_notification.py
# @Software: PyCharm
from krunner.core.android.element import AndroidElement
from krunner.core.base import ImgElement
import os


class Open_Notification(object):
    '''设置页添加push开关'''
    curr_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'template')
    return_Btn = AndroidElement(resourceId='id/left_btn', annotation='profile左上角返回')
    setmenu_Btn = AndroidElement(resourceId='id/left_btn', annotation='打开侧边栏按钮')
    setting_Btn = AndroidElement(text='设置', annotation='侧边栏设置按钮')
    push_Set = AndroidElement(text='通知设置', annotation='通知设置按钮')
    message_Btn = AndroidElement(text='评论', annotation='评论按钮')
    open_Btn = ImgElement(template=curr_dir + '/open_but.png', annotation='去开启按钮')
    # open_Btn=AndroidElement(text='去打开', annotation='去开启按钮')
    turn_on = AndroidElement(resourceId='android:id/switch_widget', annotation='开启通知开关')
