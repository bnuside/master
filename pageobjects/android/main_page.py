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
    btn_jingxuan = AndroidElement(description='精选', annotation='精选页')
    intensified_login_but = ImgElement(template=curr_dir + '/intensified_login_but.png', annotation='强化后的登录按钮')
    smile_btn_search = AndroidElement(resourceId='com.smile.gifmaker:id/right_btn', annotation='搜索按钮')
    search_find_title = AndroidElement(text='搜索发现', annotation='搜索发现标题')
    smile_search_page_back_but = AndroidElement(resourceId='com.smile.gifmaker:id/left_btn', annotation='搜索页返回按钮')

