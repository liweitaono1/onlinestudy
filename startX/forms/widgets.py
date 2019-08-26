#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: wtli
@license: MIT Licence
@contact: 1135577502@qq.com
@site: https://
@software: PyCharm
@file: widgets.py
@time: 2019-08-26
"""
from django import forms


class KindEditorInput(forms.Textarea):
    template_name = 'startX/forms/widgets/kindeditor.html'


class DateTimePickerInput(forms.TextInput):
    template_name = 'startX/forms/widgets/datetime_picker.html'
