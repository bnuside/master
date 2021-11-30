"""
@author:sunping
@time:2021/11/28:7:39 下午
"""
#!/usr/bin/env python3
import os

from krunner.core.android.element import AndroidElement
from krunner.core.base import ImgElement

class KgiPopup(object):
    curr_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'template')
    """端智能触发的弹窗手势"""

    kgi_interest_btn=AndroidElement(resourceId="id/interest_tag_dialog_title",annotation='展示兴趣标签弹窗')
    kgi_interest_game_btn=AndroidElement(text='游戏',annotation='游戏选项')
    kgi_interest_music_btn=AndroidElement(text='音乐',annotation='音乐选项')
    kgi_interest_ok_btn=AndroidElement(text='选好了(2/8)',annotation='选择了两个选项')
    kgi_interest_submit_btn=AndroidElement(resourceId='id/interest_tag_submit',annotation='点击提交按钮')
    kgi_interest_toast=AndroidElement(text='将按照您的喜好进行推荐',annotation='toast提示')

    """触发关注引导弹窗"""
    kgi_follow_btn=AndroidElement(resourceId="id/growth_follow_guide_bg",annotation='关注引导弹窗')
    kgi_follow_see=AndroidElement(text='去看看',annotation="展示去看看按钮")
    kgi_follow_later=AndroidElement(text='稍后再说',annotation='展示稍后再说按钮')
    kgi_follow_allsee=AndroidElement(text='大家都在看',annotation='跳转到大家都在看页面')

    '''触发热榜引导'''
    kgi_hot_show=AndroidElement(resourceId='id/arrow',annotation='展示热榜引导')
    kgi_hot_btn=AndroidElement(resourceId='id/text',annotation='点击热榜区域')

    kgi_search_btn=AndroidElement(resourceId='id/featured_search_hotword_view',annotation='搜索按钮点击')

    kgi_search_result=AndroidElement(resourceId='id/right_tv',annotation='搜索按钮的展示')
    kgi_search_find=AndroidElement(text='搜索发现',annotation='搜索发现的展示')








