#!/usr/bin/env python3
import os

from krunner.core.ios.element import IosElement
from krunner.core.base import ImgElement


class PrivacyPopup(object):
    """隐私弹窗"""

    curr_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'template')

    # tab_recrod = ImgElement(template=curr_dir + '/record.png', annotation='录制按钮')

    agree_button = IosElement(name='同意并继续', annotation='同意按钮')
    disagree_button = IosElement(name='不同意，进入访客模式', annotation='不同意按钮')
    disagree_again_button = IosElement(name='仍不同意', annotation='P2 页的仍不同意按钮')
    check_policy_button = IosElement(name='查看协议', annotation='查看协议按钮')
    enter_visitor_model_button = IosElement(name='进入访客模式', annotation='进入访客模式按钮')
    exit_button = IosElement(name='退出应用', annotation='进入访客模式按钮')