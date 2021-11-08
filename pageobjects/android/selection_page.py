#!/usr/bin/python3

import os

from krunner.core.android.element import AndroidElement
from krunner.core.base import ImgElement


class SelectionPage(object):
    """精选页面"""

    curr_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'template')

    like_btn = AndroidElement(description='喜欢', annotation='点赞按钮')
    comment_btn = AndroidElement(description='评论', annotation='评论按钮')
    forward_btn = AndroidElement(description='分享', annotation='分享按钮')