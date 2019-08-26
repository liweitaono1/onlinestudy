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
@time: 2019-08-26
"""
from django.urls import path

from LoginAuth import views

urlpatterns = [
 path('login', views.LoginView.as_view()),
    path('auth', views.LoginAuthView.as_view()),
    path('register', views.RegisterView.as_view()),
    path('index', views.IndexView.as_view()),

]