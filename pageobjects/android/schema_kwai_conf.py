# -*- coding: utf-8 -*- 
# @Author  :zhujungui
# @Time    :2021/11/18 11:21
# @File    :schema_kwai_conf

from krunner.core.android.element import AndroidElement

class SchemaKwaiConf(object):
    '''
    快链跳转可配置
    '''
    followTab=AndroidElement(text='关注',annotation='关注tab')
    hotTab=AndroidElement(text='发现',annotation='发现Tab')
    localTab=AndroidElement(text='同城',annotation='同城Tab')
    selectionTab=AndroidElement(text='精选',annotation='精选Tab')
    messageTab=AndroidElement(text='消息',annotation='消息Tab')
    profileTab=AndroidElement(resourceId='id/user_name_info_layout',annotation='用户信息Tab')

