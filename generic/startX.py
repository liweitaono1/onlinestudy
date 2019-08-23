#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: wtli
@license: MIT Licence
@contact: 1135577502@qq.com
@site: https://
@software: PyCharm
@file: startX.py
@time: 2019-08-23
"""
from generic.models import Account
from startX.serivce.v1 import site

site.register(Account,AccountHandler)