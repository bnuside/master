# -*- coding: utf-8 -*-
# @Time    : 2021/10/01 19:32
# @Author  : Zhujungui
# @FileName: open_notification.py
# @Software: PyCharm
from krunner.core.android.element import AndroidElement

class Open_Notification(object):
    '''设置页添加push开关'''
    return_Btn=AndroidElement(resourceId='id/left_btn',annotation='profile左上角返回')
    setmenu_Btn=AndroidElement(resourceId='com.smile.gifmaker:id/left_btn',annotation='打开侧边栏按钮')
    setting_Btn=AndroidElement(text='设置',annotation='侧边栏设置按钮')
    push_Set=AndroidElement(text='通知设置',annotation='通知设置按钮')
    message_Btn=AndroidElement(text='评论',annotation='评论按钮')
    open_Btn=AndroidElement(resourceId='com.smile.gifmaker:id/positive',annotation='去开启按钮')
    close_Btn=AndroidElement(resourceId='com.smile.gifmaker:id/close',annotation='X按钮')
    turn_on=AndroidElement(resourceId='android:id/switch_widget',annotation='开启通知开关')
    logo_text=AndroidElement(className='android.widget.TextView',annotation='快手logo')

