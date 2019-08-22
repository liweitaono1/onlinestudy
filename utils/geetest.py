#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: wtli
@license: MIT Licence
@contact: 1135577502@qq.com
@site: https://
@software: PyCharm
@file: geetest.py
@time: 2019-08-15
"""
import json
import sys

if sys.version_info >= (3,):
    xrange = range

VERSION = '3.0.0'


class GeetestLib(object):
    FN_CHALLENGE = "geetest_challenge"
    FN_VALIDATE = 'geetest_validate'
    FN_SECCODE = 'geetest_seccode'
    GT_STATUS_SESSION_KEY = 'gt_server_status'
    API_URL = "http://api.geetest.com"
    REGISTER_HANDLER = "/register.php"
    VALIDATE_HANDLER = "/validate.php"
    JSON_FORMAT = False

    def __init__(self, captcha_id, private_key):
        self.private_key = private_key
        self.captcha_id = captcha_id
        self.sdk_version = VERSION
        self._response_str = ""

    def pre_process(self, user_id=None, new_captcha=1, JSON_FORMAT=1, client_type='web', ip_address=''):
        '''
        验证初始化预处理
        :param user_id:
        :param new_captcha:
        :param JSON_FORMAT:
        :param client_type:
        :param ip_address:
        :return:
        '''
        status, challenge = self._register(user_id, new_captcha, JSON_FORMAT, client_type, ip_address)
        self._response_str = self._make_response_format(status, challenge, new_captcha)
        return status

    def _register(self, user_id=None, new_captcha=1, JSON_FORMAT=1, client_type='web', ip_address=''):
        pri_responce = self._register_challenge(user_id, new_captcha, JSON_FORMAT, client_type, ip_address)
        if pri_responce:
            if JSON_FORMAT == 1:
                response_dic = json.loads(pri_responce)
                challenge = response_dic['challenge']
            else:
                challenge = pri_responce
        else:
            challenge = ' '
        if len(challenge) == 32:
            challenge = self._md5_encode(''.join([challenge,self.private_key]))
            return 1,challenge
        else:
            return 0,self._make_fail_challenge()

    def get_response_str(self):
        return self._response_str
