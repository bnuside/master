"""

======================

@author:sunping

@time:2021/11/26:8:11 下午

======================

"""
import json
import time,os

import requests
from krunner.utils import logger
from krunner.utils import adb
from krunner.conf import get_config_value
from pageobjects.android.privacy_popup import PrivacyPopup
from pageobjects.android.interest_popup import InterestPopup
from testcase.krunner import KRunner
from krunner.plugins.mock import Mock
# 添加AB白名单基础方法
def addOrDeleteAbtest(mode, worldName, exp_name, group_name, deviceId='', userId=''):
    """
    添加ABtest分组白名单，支持uid和did
    cookie目前失效时间为1年，在接口访问失败后需要更换 cookie
    :param mode: add 或delete
    :param worldName: AB世界名字，str
    :param exp_name: 实验名，str
    :param group_name: 分组名，base1,base2,exp1等，str
    :param deviceId: 设备did
    :param userId: 用户ID
    :return:
    """
    def getCookies():
        url = 'http://172.17.142.23:8080/getabtestcookies'
        # url = 'http://172.17.142.39:8080/getabtestcookies'
        try:
            cookieRequests = requests.get(url=url)
            statusCode = cookieRequests.status_code
            cookiesDict = {'apdid': None, '_did': None, 'accessproxy_session': None, 'JSESSIONID': None,
                           'username': None, 'ou': None, 'uuid': None, 'userToken': None}
            if statusCode == 200:
                cookies = json.loads(cookieRequests.text)
                for item in cookies:
                    if item['name'] == 'apdid':
                        cookiesDict['apdid'] = item['value']
                    elif item['name'] == '_did':
                        cookiesDict['_did'] = item['value']
                    elif item['name'] == 'accessproxy_session':
                        cookiesDict['accessproxy_session'] = item['value']
                    elif item['name'] == 'JSESSIONID':
                        cookiesDict['JSESSIONID'] = item['value']
                    elif item['name'] == 'username':
                        cookiesDict['username'] = item['value']
                    elif item['name'] == 'ou':
                        cookiesDict['ou'] = item['value']
                    elif item['name'] == 'uuid':
                        cookiesDict['uuid'] = item['value']
                    elif item['name'] == 'userToken':
                        cookiesDict['userToken'] = item['value']
                logger.info('cookies:' + str(cookiesDict))
                return cookiesDict
        except:
            logger.info('获取cookies失败')
            return None
    def sendPostMessage(mode, worldName, exp_name, group_name, deviceId='', userId=''):
        baseUrl = 'https://abtest.corp.kuaishou.com/rest/i/abtest/whitelist/' + mode
        #获取cookie内容
        cookiesD = getCookies()
        if cookiesD != None:
            logger.info('cookie有更新')
            apdid = str(cookiesD['apdid'])
            did = str(cookiesD['_did'])
            accessproxy_session = str(cookiesD['accessproxy_session'])
            JSESSIONID = str(cookiesD['JSESSIONID'])
            username = str(cookiesD['username'])
            ou = str(cookiesD['ou'])
            uuid = str(cookiesD['uuid'])
            userToken = str(cookiesD['userToken'])
            logger.info('获取值' + 'apdid=' + apdid + '\n_did=' + did + '\naccessproxy_session=' + accessproxy_session + '\nJSESSIONID=' + JSESSIONID + '\nuserToken=' + userToken)
        else:
            logger.info('cookie无更新')
            apdid = 'f96e5068-d1c4-4258-a9a5-9b7618b269659eabb1f04847d5be2480854e599ab382:1616297866:1'
            did = 'web_9117143851B827C0'
            accessproxy_session = '9ad79999-6adc-40e4-80cb-bd5923f270d8'
            JSESSIONID = 'BD5A83073CB5AC30CF2FDE2982A0C464'
            username = 'mashikai'
            ou = 'ks|6250-18-12-6254-6251'
            uuid = '4cbd8b94cf067d86830d125568bf424c'
            userToken = 'm9ilp+IxHj4uhvODa8HG+Q==-mashikai'
        headers = {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '160',
            'Content-Type': 'application/json;charset=UTF-8',
            'Cookie': 'apdid=' + apdid +'; ksCorpDeviceid=ca4af250-af28-4060-812f-eaa1d5c68ea0; _did=' + did + '; Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee=1616655170; clientid=3; did=web_635981e2c3e4f2e5956212c14299c999; client_key=65890b29; accessproxy_session='+ accessproxy_session + '; JSESSIONID=' + JSESSIONID + '; username=' + username + '; ou=' + ou + '; uuid=' + uuid + '; userToken=' + userToken + '; userName=' + username,
            'Host': 'abtest.corp.kuaishou.com',
            'Origin': 'https://abtest.corp.kuaishou.com',
            'Referer': 'https://abtest.corp.kuaishou.com/',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        logger.info('headers: ' + str(headers))
        logger.info('使用值 apdid=' + apdid + '\n_did=' + did + '\naccessproxy_session=' + accessproxy_session + '\nJSESSIONID=' + JSESSIONID + '\nuserToken=' + userToken)
        data = None
        if mode == 'add':
            if deviceId != '':
                data = {'world_name': worldName, 'experiment_name': exp_name,'group_name': group_name, 'group_device_ids': [deviceId], 'confirm_type': 0}

            elif userId != '':
                data = {'world_name': worldName, 'experiment_name': exp_name, 'group_name': group_name,
                        'group_user_ids': [userId], 'confirm_type': 0}
        elif mode == 'delete':
            if deviceId != '':
                data = {"world_name": worldName, "experiment_name": exp_name,"group_name": group_name, "group_device_ids": [deviceId], "group_user_ids": []}
            elif userId != '':
                data = {"world_name": worldName, "experiment_name": exp_name, "group_name": group_name,
                        "group_user_ids": [userId]}
        if data != None:
            logger.info('添加信息：' + str(data))
            r = requests.post(url=baseUrl, headers=headers, data=json.dumps(data))
            return r.text

    jsonRText = json.loads(sendPostMessage(mode=mode, worldName=worldName, exp_name=exp_name, group_name=group_name, deviceId=deviceId, userId=userId))

    logger.info('接口返回内容：' + str(jsonRText))
    if jsonRText['result'] == 1:
        logger.info('done')
        return True
    elif jsonRText['result'] == 301:
        logger.info('已在其他白名单中，先删除白名单')
        stayExp_name = jsonRText['error_msg'].split('->')[-1].split(':')[0].strip()
        stayGroup_name = jsonRText['error_msg'].split('->')[-1].split(':')[1].strip()
        logger.info('删除结果：' + sendPostMessage(mode='delete', worldName=worldName, exp_name=stayExp_name, group_name=stayGroup_name, deviceId=deviceId,userId=userId))
        logger.info('再次添加白名单')
        time.sleep(2)
        jsonRText = json.loads(sendPostMessage(mode=mode, worldName=worldName, exp_name=exp_name, group_name=group_name,
                                               deviceId=deviceId, userId=userId))
        logger.info('再次添加结果：' + str(jsonRText))
        if jsonRText['result'] == 1:
            logger.info('done')
            return True
        else:
            logger.info('errorMessage:' + jsonRText)
            return False
    else:
        logger.info('errorMessage:' + jsonRText)
        return False

