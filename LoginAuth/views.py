import hashlib
import uuid

import redis
from django.shortcuts import render
from rest_framework.response import Response

from LoginAuth.serializers import RegisterSerializer
from generic.models import Account
from utils.Auther import Auther
# Create your views here.
from rest_framework.views import APIView

from utils.BaseResponse import BaseResponse
from utils.redis_pool import POOL

pc_geetest_id = "64936e8e1ad53dad8bbee6f96224e7d0"
pc_geetest_key = "8322ed330d370a704a77d8205c94d20f"
RedisConn = redis.Redis(connection_pool=POOL)


class IndexView(APIView):
    '''后端测试的接口'''
    authentication_classes = [Auther, ]

    def get(self, request):
        return Response('首页,欢迎%s' % request.user.username)


class RegisterView(APIView):
    '''
    注册
    '''

    def post(self, request):
        res = BaseResponse()
        user_obj = RegisterSerializer(data=request.data)
        if user_obj.is_valid():
            user_obj.save()
            res.data = user_obj.data
        else:
            res.code = -1
            res.error = user_obj.errors
        return Response(res.dict)


class LoginView(APIView):
    '''
    登录
    '''

    def post(self, request):
        res = BaseResponse()
        username = request.data.get('username')
        passwd = request.data.get('passwd')
        # 密码加盐
        hash_key = 'password'
        passwd = passwd + hash_key
        passwd_md5 = hashlib.md5(passwd.encode()).hexdigest()
        user_obj = Account.objects.filter(username=username, passwd=passwd_md5).first()
        if not user_obj:
            res.code = 1030
            res.error = '用户名密码不匹配'
        try:
            token = uuid.uuid4()
            RedisConn.set(str(token), user_obj.id)
            shop_cart = ShoppingView().get(request)
            # 购物车数据
            res.data = {
                'access_token': token,
                'avatar': 'http://127.0.0.1:8000/media/avatar.png',
                'username': user_obj.username,
                'shop_cart_num': shop_cart.data.get('data'),
                'balance': user_obj.balance
            }
            # 头像, 购物车数据, token, 用户名, 账户余额
        except Exception as e:
            print('........', e)
            res.code = 1031
            res.error = '创建令牌失败'
        return Response(res.dict)


class LoginAuthView(APIView):
    def get(self,request):
        user_id = 'Auth_'
        gt = GeetestLib
