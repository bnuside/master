#!/usr/bin/python3

import os

from krunner.core.android.element import AndroidElement
from krunner.core.base import ImgElement


class RankPage(object):
    """快手热榜页面"""

    curr_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'template')

    left_btn = AndroidElement(description='返回', annotation='左上角返回按钮')
    rank_tab = AndroidElement(text='热榜', annotation='热榜tab')
    tiaozhan_tab = AndroidElement(text='挑战榜', annotation='挑战榜tab')
