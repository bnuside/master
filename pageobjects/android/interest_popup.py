#!/usr/bin/env python3
import os

from krunner.core.android.element import AndroidElement
from krunner.core.base import ImgElement

class InterestPopup(object):
    """兴趣标签弹窗"""

    curr_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'template')

    # tab_recrod = ImgElement(template=curr_dir + '/record.png', annotation='录制按钮')
    # agree_button = AndroidElement(resourceId='com.smile.gifmaker:id/positive', description='同意并继续', annotation='同意按钮')
    #agree_button = AndroidElement(text='同意并继续', annotation='同意按钮')
    # disagree_button = AndroidElement(text='不同意', annotation='不同意按钮')
    # disagree_again_button = AndroidElement(text='仍不同意', annotation='P2 页的仍不同意按钮')
    # check_policy_button = AndroidElement(text='查看协议', annotation='查看协议按钮')
    # enter_visitor_model_button = AndroidElement(text='进入访客模式', annotation='进入访客模式按钮')
    # exit_button = AndroidElement(text='退出应用', annotation='进入访客模式按钮')
    """通过元素定位进入设置页"""

    # return_back = AndroidElement(description='返回', index=0, annotation='返回按钮')
    # menu_btn=AndroidElement(resourceId='com.smile.gifmaker:id/left_btn',annotation='菜单按钮')
    # set_btn=AndroidElement(resourceId='com.smile.gifmaker:id/setting_iv',annotation='设置按钮')
    # about_btn=AndroidElement(text='关于我们',annotation='关于我们按钮')
    #logo_btn=AndroidElement(resourceId='com.smile.gifmaker:id/logo',annotation='快手图标')
    """兴趣标签元素定位"""

    interest_btn=AndroidElement(resourceId="com.smile.gifmaker:id/interest_tag_dialog_title",annotation='兴趣标签弹窗')
    interest_game_btn=AndroidElement(text='游戏',annotation='游戏选项')
    interest_music_btn=AndroidElement(text='音乐',annotation='音乐选项')
    interest_any_btn=AndroidElement(resourceId='com.smile.gifmaker:id/interest_tag_item_text',annotation='选择明星娱乐选项')
    interest_submit_btn=AndroidElement(resourceId='com.smile.gifmaker:id/interest_tag_submit',annotation='提交兴趣标签')

    interest_all_btn=AndroidElement(text='全部标签',annotation='点击全部标签')
    interest_ok_btn=AndroidElement(resourceId="com.smile.gifmaker:id/milano_player_seekbar",annotation='选好了')
    interest_toast_btn=AndroidElement(text='将按照您的喜好进行推荐',annotation='toast提示"')
    interest_close_btn=AndroidElement(resourceId='com.smile.gifmaker:id/interest_tag_close',annotation="点击关闭按钮")



