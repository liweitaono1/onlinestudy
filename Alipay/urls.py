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
from django.urls import path

from Alipay.views import AlipayView, PayHandlerView

urlpatterns = [
    path('pay/', AlipayView.as_view()),
    path('alipay_handler', PayHandlerView.as_view())
]
