#!/usr/bin/env python3
import os

from krunner.core.android.element import AndroidElement
from krunner.core.base import ImgElement


class AboutUs(object):
    """快手设置页"""

    curr_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'template')

    # tab_recrod = ImgElement(template=curr_dir + '/record.png', annotation='录制按钮')
    # agree_button = AndroidElement(resourceId='com.smile.gifmaker:id/positive', description='同意并继续', annotation='同意按钮')
    version = AndroidElement(resourceId='id/version_tv', annotation='「版本号」标签')
    channel = AndroidElement(resourceId='id/channel', annotation='「渠道号」标签')
