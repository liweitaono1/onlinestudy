#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: wtli
@license: MIT Licence
@contact: 1135577502@qq.com
@site: https://
@software: PyCharm
@file: urls.py
@time: 2019-08-22
"""
from django.urls import path, re_path

from blwvideo.views import Polyv, test_bolyv

urlpatterns = [
    path('polyv', Polyv.as_view()),
    re_path(r'^crossdomain.xml', test_bolyv)
]
