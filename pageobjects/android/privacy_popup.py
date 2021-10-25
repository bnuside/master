#!/usr/bin/env python3
import os

from krunner.core.android.element import AndroidElement
from krunner.core.base import ImgElement


class PrivacyPopup(object):
    """隐私弹窗"""

    curr_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'template')

    # tab_recrod = ImgElement(template=curr_dir + '/record.png', annotation='录制按钮')
    # agree_button = AndroidElement(resourceId='com.smile.gifmaker:id/positive', description='同意并继续', annotation='同意按钮')
    agree_button = AndroidElement(text='同意并继续', annotation='同意按钮')
    disagree_button = AndroidElement(text='不同意', annotation='不同意按钮')
    disagree_again_button = AndroidElement(text='仍不同意', annotation='P2 页的仍不同意按钮')
    check_policy_button = AndroidElement(text='查看协议', annotation='查看协议按钮')
    enter_visitor_model_button = AndroidElement(text='进入访客模式', annotation='进入访客模式按钮')
    exit_button = AndroidElement(text='退出应用', annotation='进入访客模式按钮')
