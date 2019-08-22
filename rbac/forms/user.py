#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: wtli
@license: MIT Licence
@contact: 1135577502@qq.com
@site: https://
@software: PyCharm
@file: user.py
@time: 2019-08-15
"""
from django import forms
from rest_framework.exceptions import ValidationError

from rbac.forms.base import BaseForm
from rbac.models import User


class UserModelForm(BaseForm):
    confirm_password = forms.CharField(label='确认密码')

    class Meta:
        model = User
        fields = ['username', 'email', 'passwd', 'confirm_password']

    def clean_confirm_password(self):
        passwd = self.cleaned_data['passwd']
        confirm_password = self.cleaned_data['confirm_password']
        if passwd != confirm_password:
            raise ValidationError('两次密码不一致')
        return confirm_password


class UpdateUserModelForm(forms.ModelForm):
    confirm_password = forms.CharField(label='确认密码')

    class Meta:
        model = User
        fields = ['username', 'email', ]


class ResetUserModelForm(forms.ModelForm):
    confirm_password = forms.CharField(label='确认密码')

    class Meta:
        model = User
        fields = ['passwd', 'confirm_password']

    def clean_confirm_password(self):
        passwd = self.cleaned_data['passwd']
        confirm_password = self.cleaned_data['confirm_password']

        if passwd != confirm_password:
            raise ValidationError('两次密码不一致')
        return confirm_password
