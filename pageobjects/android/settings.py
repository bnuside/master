#!/usr/bin/env python3
import os

from krunner.core.android.element import AndroidElement
from krunner.core.base import ImgElement


class Settings(object):
    """快手设置页"""

    curr_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'template')

    # tab_recrod = ImgElement(template=curr_dir + '/record.png', annotation='录制按钮')
    # agree_button = AndroidElement(resourceId='com.smile.gifmaker:id/positive', description='同意并继续', annotation='同意按钮')
    about_us = AndroidElement(text='关于我们', annotation='「关于我们」按钮')
