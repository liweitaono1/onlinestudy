#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: wtli
@license: MIT Licence
@contact: 1135577502@qq.com
@site: https://
@software: PyCharm
@file: role.py
@time: 2019-08-15
"""
from django import forms

from rbac.models import Role


class RoleModelForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['title', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }
