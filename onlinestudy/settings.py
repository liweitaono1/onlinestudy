"""
Django settings for onlinestudy project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5w83cc1hz)yqmwg!2!f76v6!xlm^ol#50(nf34t_ca8#py@6ct'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'generic.apps.GenericConfig',
    'rest_framework',
    'corsheaders',
    'startX.apps.StartxConfig',
    'rbac.apps.RbacConfig',
    'blwvideo',
    'LoginAuth',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'rbac.middlewares.rbac.RbacMiddleware',
    # 'utils.middlewares.MyCors',
]

ROOT_URLCONF = 'onlinestudy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'onlinestudy.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '123456',
        'NAME': 'onlinestudy',
        # 'OPTIONS': {
        #     'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        # },
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = ('*')

CORS_ALLOW_METHODS = (

    'DELETE',

    'GET',

    'OPTIONS',

    'PATCH',

    'POST',

    'PUT',

    'VIEW',

)

CORS_ALLOW_HEADERS = (

    'XMLHttpRequest',

    'X_FILENAME',

    'accept-encoding',

    'authorization',

    'content-type',

    'dnt',

    'origin',

    'user-agent',

    'x-csrftoken',

    'x-requested-with',

    'Pragma',

)

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# --------- 保利威视频注册用户id和key--------

POLYV_CONFIG = {
    'userId': '2f57a43618',  # polyv 提供的服务器间的通讯验证
    'secretkey': 'Uh9Ezw7Wdq'  # polyv 提供的接口调用签名访问的key
}

# ############ 作业文件url ####
BASE_FILE = 'http://127.0.0.1:8000/media/'

# ############ 权限配置相关 #########

RBAC_USER_MODLE_CLASS = "generic.models.Account"

# 自动化发现路由中URL时，排除的URL
AUTO_DISCOVER_EXCLUDE = [
    '/admin/.*',
    '/login/',
    '/logout/',
    '/index/',
    '/api/v1/.*',  # 与前端交互的api接口
    '/media/.*',  # 静态文件url
    '/blv/polyv.*',  # 保利威视频
    '/polyv.*'
]

INIT_PERMISSION = "XXX_permission_url_list_key"
INIT_MENU = "XXX_permission_menu_key"
# 需要登录但无需权限的URL
NO_PERMISSION_LIST = [
    '/index/',
    '/logout/',
]
# 白名单，无需登录就可以访问：
VALID_URL = [
    '/login/',
    '/admin/.*',
    '/api/v1/.*',  # 与前端交互的api接口
    '/media/.*',  # 静态文件url
    '/blv/polyv.*',  # 保利威视频
    '/polyv.*',
    '/upload.*'

]
# ######## 用户趋势图 #######
TREND_URL = 'http://127.0.0.1:8000/account/trend/%d'

# ######## 订单趋势图 #######
ORDER_URL = 'http://127.0.0.1:8000/order/trend/%d'
