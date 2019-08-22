#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: wtli
@license: MIT Licence
@contact: 1135577502@qq.com
@site: https://
@software: PyCharm
@file: redis_pool.py
@time: 2019-08-15
"""

import redis

POOL = redis.ConnectionPool(host='127.0.0.1', decode_responses=True, max_connections=20)
