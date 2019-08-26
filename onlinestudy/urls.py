"""onlinestudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from LoginAuth.views import login, logout, index, upload, account_trend, order_trend
from serivce.v1 import site

urlpatterns = [
    path('login/', login),
    path('logout/', logout),
    path('index/', index),
    path('upload/', upload),
    path('api/v1/', include(('generic.urls', 'generic'))),
    path('api/v1/auth/', include(('LoginAuth.urls', 'LoginAuth'))),  # 登录认证
    path('api/v1/pay/', include(('Alipay.urls', 'Alipay'))),  # 支付宝支付
    path('blv/', include(('blwvideo.urls', 'blwvideo'))),  # 保利威加密视频接口
    path('admin/', admin.site.urls),
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^account/trend/(?P<year>\d+)/$', account_trend, name='account_trend'),
    re_path(r'^order/trend/(?P<year>\d+)/$', order_trend, name='order_trend'),
    re_path(r'^rbac/', include(('rbac.urls', 'rbac'))),  # 权限配置
    path('backend/', site.urls),  # 后台相关管理
]
