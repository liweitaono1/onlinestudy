#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: wtli
@license: MIT Licence
@contact: 1135577502@qq.com
@site: https://
@software: PyCharm
@file: startX.py
@time: 2019-08-23
"""
from generic.handlers.account import AccountHandler
from generic.handlers.article import ArticleHandler
from generic.handlers.consult_record import ConsultRecordHandler
from generic.handlers.course import CourseHandler
from generic.handlers.course_chapter import CourseChapterHandler
from generic.handlers.course_coupon import CourseCouponHandler
from generic.handlers.course_detail import CourseDetailHandler
from generic.handlers.course_lesson import CourseLessonHandler
from generic.handlers.course_outline import CourseOutlineHandler
from generic.handlers.course_price import CoursePriceHandler
from generic.handlers.homework import HomeworkHandler
from generic.handlers.homework_detail import HomeworkDetailHandler
from generic.handlers.order import OrderHandler
from generic.handlers.order_trend import OrderTrendHandler
from generic.handlers.ordertail import OrderDetailHandler
from generic.handlers.payment_record import PaymentRecordHandler
from generic.handlers.question import QuestionHandler
from generic.handlers.register_trend import AccountRegisterTrendHandler
from generic.handlers.student import StudentHandler
from generic.handlers.study_record import StudyRecordHandler
from generic.handlers.tutor import TutorHandler
from generic.models import Account, StudyRecord, HomeworkDetail, StudyQuestion, Homework, Article, ConsultRecord, Tutor, \
    Student, PaymentRecord, OrderDetail, Order, CourseLesson, PricePolicy, Coupon, CourseChapter, CourseOutline, \
    CourseDetail, Course
from startX.serivce.v1 import site

site.register(Account, AccountHandler)
site.register(Account, AccountRegisterTrendHandler, prev='trend')
site.register(Course, CourseHandler)
site.register(CourseDetail, CourseDetailHandler)
site.register(CourseOutline, CourseOutlineHandler)
site.register(CourseChapter, CourseChapterHandler)
site.register(Coupon, CourseCouponHandler)
site.register(PricePolicy, CoursePriceHandler)
site.register(CourseLesson, CourseLessonHandler)
site.register(Order, OrderHandler)
site.register(Order, OrderTrendHandler, prev='trend')
site.register(OrderDetail, OrderDetailHandler)
site.register(PaymentRecord, PaymentRecordHandler)
site.register(Student, StudentHandler)
site.register(Tutor, TutorHandler)
site.register(ConsultRecord, ConsultRecordHandler)
site.register(Article, ArticleHandler)
site.register(Homework, HomeworkHandler)
site.register(StudyQuestion, QuestionHandler)
site.register(HomeworkDetail, HomeworkDetailHandler)
site.register(StudyRecord, StudyRecordHandler)
