#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: wtli
@license: MIT Licence
@contact: 1135577502@qq.com
@site: https://
@software: PyCharm
@file: BaseResponse.py
@time: 2019-08-15
"""


class BaseResponse(object):
    def __init__(self):
        self.code = None
        self.data = None
        self.error = None

    @property
    def dict(self):
        return self.__dict__
