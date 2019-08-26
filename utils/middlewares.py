#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: wtli
@license: MIT Licence
@contact: 1135577502@qq.com
@site: https://
@software: PyCharm
@file: middlewares.py
@time: 2019-08-26
"""
from django.utils.deprecation import MiddlewareMixin


class MyCors(MiddlewareMixin):
    def process_response(self,request,response):
        response['Access-Control-Allow-Origin'] = '*'
        if request.method == 'OPTIONS':
            response["Access-Control-Allow-Headers"] = "*"
            response['Access-Control-Allow-Methods'] = '*'
        return response

