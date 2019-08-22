#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: wtli
@license: MIT Licence
@contact: 1135577502@qq.com
@site: https://
@software: PyCharm
@file: polyv.py
@time: 2019-08-22
"""
import hashlib
import time

import requests
from django.conf import settings


class PolyvPlayer(object):
    userId = settings.POLYV_CONFIG['userId']
    secretkey = settings.POLYV_CONFIG['secretkey']

    def tomd5(self, value):
        return hashlib.md5(value.encode()).hexdigest()

    def get_video_token(self, videoId, viewerIp, viewerId=None, viewerName='', extraParams='HTML5'):
        '''

        :param videoId: 视频id
        :param viewerIp: 看视频用户id
        :param viewerId: 看视频用户ip
        :param viewerName: 看视频用户昵称
        :param extraParams: 扩展参数
        :return: sign:加密的sign
        :return: 返回点播的视频的token
        '''

        ts = int(time.time() * 1000)  # 时间戳
        plain = {
            'userId': self.userId,
            'videoId': videoId,
            'ts': ts,
            'viewerId': viewerId,
            'viewerIp': viewerIp,
            'viewerName': viewerName,
            'extraParams': extraParams
        }
        plain_sorted = {}
        key_temp = sorted(plain)
        for key in key_temp:
            plain_sorted[key] = plain[key]
        print(plain_sorted)

        plain_string = ''
        for k, v in plain_sorted.items():
            plain_string += str(k) + str(v)
        print(plain_string)

        sign_data = self.secretkey + plain_string + self.secretkey

        # 取sign_data的md5的大写
        sign = self.tomd5(sign_data).upper()

        # 新的带有sign的字典
        plain.update({'sign': sign})
        result = requests.post(url='https://hls.videocc.net/service/v1/token',
                               headers={'Content-type': 'application/x-www-form-urlencoded'}, data=plain).json()
        data = {} if isinstance(result, str) else result.get('data', {})
        return {'token': data}

    def get_play_key(self, vid, username, code, status, ts):
        '''

        :param vid: 视频 vid
        :param username: 响应跑马灯展示
        :param code: 自定义参数
        :param status: 是否可播放, 1,可播放 2,禁播
        :param ts: 时间戳
        :return:
        '''
        return self.tomd5(
            ('vid={}&secretkey={}&username={}&code={}&status={}&t={}').format(vid, self.secretkey, username, code,
                                                                              status, ts)).lower()

    @staticmethod
    def get_resp(status, username, sign, msg='授权暂未通过'):
        res_str = {
            'status': status,
            'username': username,
            'sign': sign,
            'msg': msg,
            'fontSize': '18',
            'fontColor': '0xFF0000',
            'speed': '50',
            'filter': 'on',
            'setting': '2',
            'alpha': '0.7',
            'filterColor': '0x3914AF',
            'blurX': '2',
            'blurY': '2',
            'tweenTime': '1',
            'interval': '3',
            'lifeTime': '3',
            'strength': '4',
            'show': 'on'
        }
        return res_str


polyv_video = PolyvPlayer()