#!/usr/bin/env python3
import os

from krunner.core.android.element import AndroidElement
from krunner.core.base import ImgElement


class MainPage(object):
    """快手APP首页"""

    curr_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'template')

    tab_recrod = ImgElement(template=curr_dir + '/record.png', annotation='录制按钮')
    btn_find = AndroidElement(description='发现', annotation='发现页')
    btn_guanzhu = ImgElement(template='关注', annotation='关注页')