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
from django.urls import path,re_path
from generic import views

urlpatterns = [
    path('category', views.CategoryView.as_view()),
    path('course', views.CourseView.as_view()),
    path('degree', views.DegreeView.as_view()),
    path('detail/<int:pk>', views.CourseDetailView.as_view()),
    path('chapter/<int:pk>', views.CourseChapterView.as_view()),
    path('comment/<int:pk>', views.CourseCommentView.as_view()),
    path('commonquestion/<int:pk>', views.CourseCommonquestionView.as_view()),
    path('shopping', views.ShoppingView.as_view()),
    path('settlement', views.SettlementView.as_view()),
    path('payment', views.PaymentView.as_view()),
    path('coupon', views.CouponDistributionView.as_view()),
    path('usercoupon', views.UserCouponView.as_view()),
    path('usercourse', views.UserCourseView.as_view()),
    path('question', views.QuestionView.as_view()),
    path('homework', views.HomeworkView.as_view()),
    path('article', views.ArticleView.as_view()),
]