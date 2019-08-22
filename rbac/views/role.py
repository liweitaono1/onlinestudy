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
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from rbac.forms.role import RoleModelForm
from rbac.models import Role


def role_list(request):
    roles = Role.objects.all()
    return render(request, 'rbac/role_list.html', {'roles': roles})


# 添加,修改,删除
def role_add(request):
    if request.method == 'GET':
        form = RoleModelForm()
        return render(request, 'rbac/change.html', {'form': form})
    form = RoleModelForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('rbac:role_list'))
    return render(request, 'rbac/change.html', {'form': form})


def role_edit(request, id):
    obj = Role.objects.filter(id=id).first()
    if not obj:
        return HttpResponse('不存在该用户')
    if request.method == 'GET':
        form = RoleModelForm(instance=obj)
        return render(request, 'rbac/change.html', {'form': form})
    form = RoleModelForm(instance=obj, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('rbac:role_list'))
    return render(request, 'rbac/change.html', {'form': form})


def role_del(request, id):
    cancel = reverse('rbac:role_list')
    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel': cancel})
    Role.objects.filter(id=id).delete()
    return redirect(cancel)
