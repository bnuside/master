#!/usr/bin/python3

import os

from krunner.core.android.element import AndroidElement
from krunner.core.base import ImgElement


class GrowthCleaner(object):
    """垃圾清理及清理完成页面"""

    curr_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'template')
    entry = ImgElement(template=curr_dir + '/cleaner_long_click.png', annotation='垃圾待清理入口')
    scan_btn = AndroidElement(textContains='扫描垃圾', annotation='扫描垃圾按钮')
    cleaner_selected_btn = AndroidElement(textContains='清理选中垃圾', annotation='清理选中垃圾按钮')
    cleaner_not_selected_btn = AndroidElement(text='完成', annotation='不清理垃圾')
    rescan_btn = AndroidElement(text='重新扫描', annotation='重新扫描按钮')
    hot_rank_btn = AndroidElement(text='今日热榜', annotation='热榜入口')
    selection_btn = AndroidElement(text='刷精选', annotation='精选入口')
    find_btn = AndroidElement(text='看发现', annotation='发现入口')
    record_btn = AndroidElement(text='拍一拍', annotation='拍摄入口')
