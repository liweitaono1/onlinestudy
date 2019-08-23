#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: wtli
@license: MIT Licence
@contact: 1135577502@qq.com
@site: https://
@software: PyCharm
@file: account.py
@time: 2019-08-23
"""
from generic.models import Account
from serivce.v1 import StartXModelForm, StartXHandler


class AccountModelForm(StartXModelForm):
    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'level']


class AccountHandler(PermissionHandler, StartXHandler):
    order_by = ['level', 'id']
    model_form_class = AccountModelForm
    list_display = ['username', 'email', 'brief', get_field_display('学历', 'education'), 'career',
                    get_field_display('用户等级', 'level')]
    search_list = ['username__contains']
