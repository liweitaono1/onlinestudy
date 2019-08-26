#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: wtli
@license: MIT Licence
@contact: 1135577502@qq.com
@site: https://
@software: PyCharm
@file: md5.py
@time: 2019-08-26
"""

import hashlib


def gen_md5(value):
    hash_key = 'password'
    res = value + hash_key
    res = hashlib.md5(res.encode()).hexdigest()
    return res
