from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class GenericConfig(AppConfig):
    name = 'generic'

    def ready(self):
        '''
        通过看django的源码可以得知：Django启动时，自动加载settings配置文件中的installed_apps，然后执行源码中的autodiscover()
        方法来顺序加载apps对应的admin.py文件。所以我们可以通过修改apps中的代码让django来执行我们写的starX.py文件而不执行admin.py文件.
        '''
        autodiscover_modules('startX')
