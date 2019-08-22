from django.db import models

# Create your models here.
from rbac.models import User as RBACUser


class Account(RBACUser):
    '''
    用户表
    '''
    brief = models.CharField(max_length=64, verbose_name='学员简介', null=True, blank=True)
    CHOICES = ((0, '大专'), (1, '本科'), (2, '研究生'), (3, '博士'), (4, '硕士'), (5, '其他'))
    education = models.IntegerField(choices=CHOICES, verbose_name='学历', null=True, blank=True)
    career = models.CharField(max_length=32, verbose_name='目前职业/最近一次从事职业', null=True, blank=True)
    balance = models.IntegerField(verbose_name='账户余额', default=0)
    LEVEL_CHOICES = ((0, '管理员'), (1, '导师'), (2, '学员'), (3, '非学员'))
    level = models.IntegerField(choices=LEVEL_CHOICES, default=3, verbose_name='用户等级')
    date = models.DateTimeField(verbose_name='注册日期', auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = 'DB_Account'
        db_table = verbose_name_plural
