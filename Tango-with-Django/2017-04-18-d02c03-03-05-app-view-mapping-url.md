# Django

- 如何建立 Django Application(应用)
- 如何建立 View
- 如何 mapping url

## 1 Application

Django的项目是 configurations 和 application 的集合.

之前已经建立了一个项目, 那么如何在这个项目中建立一个 app 呢？

打开 PS, 进入虚拟环境 rango 下, 到我们之前建立的 *tango_with_django_project* 目录下, 执行

`$ python manage.py startapp rango` 

在项目 *tango_with_django_project* 下我们建立了名为 *rango* 的 app.

```
    目录: E:\2016-for_Vocation\gopython\Tango-with-Django\tango_with_django_project

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        2017/4/18      8:18                rango
d-----        2017/4/17     15:28                tango_with_django_project
-a----        2017/4/17     15:28           3072 db.sqlite3
-a----        2017/4/17     15:16            823 manage.py
```

在 这个 *rango* 有下面几个 file:

```
    目录: E:\2016-for_Vocation\gopython\Tango-with-Django\tango_with_django_project\rango

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        2017/4/18      8:18                migrations
-a----        2017/4/18      8:18             63 admin.py
-a----        2017/4/18      8:18            126 apps.py
-a----        2017/4/18      8:18             98 models.py
-a----        2017/4/18      8:18             60 tests.py
-a----        2017/4/18      8:18             63 views.py
-a----        2017/4/18      8:18              0 __init__.py
```

其中:

```
__init__.py # 空脚本, 它的存在为了表明当前这个directiory目录是 Python 包.
admin.py    # where you can register your models so that you can benefit from some 
            # Django machinery which creates an admin interface for you;
apps.py     # that provides a place for any **application specific configuration**
models.py   # a place to store your application’s **data models**
tests.py    # where you can store a series of functions to test your 
            # application’s code
views.py    # 填写我们的请求 requests 和 response 
            # where you can store a series of functions that handle 
            # requests and return responses
migrations  # 文件目录, which stores database specific information 
            # related to your models.
```

具体执行后增加的文件代码如[python manage.py startapp rango :dancer: · JeremiahZhang/gopython@e1365aa](https://github.com/JeremiahZhang/gopython/commit/e1365aa2c84b06b02743b9845c4014167a6f1a40)所示

建立好app 后需要修改 *Tango-with-Django/tango_with_django_project/tango_with_django_project/* 项目中的 **settings.py** 文件

```
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rango',                         # 添加这一行
]
```

可参考 [add rango app · JeremiahZhang/gopython@bd56ab1](https://github.com/JeremiahZhang/gopython/commit/bd56ab186e696086a2ea4eed196bc7efb3f91165)

难道不能自动添加么?不过自动添加了, 我们也要查看一下 rango 这个app在不在里面 application definition 里面.

## 2 View

既然建立 rango app 我们已经完成, 如何让我们在浏览器中看见view到我们想要表示出来的内容呢?这时候就需要修改 rango 目录下的 `views.py`, 同时需要项目 *Tango-with-Django/tango_with_django_project/tango_with_django_project/* 中的 `urls.py` 参考 [Django rango create a view](https://github.com/JeremiahZhang/gopython/commit/b994fa68b501af476ef898dfa639a884907b378b)


*Tango-with-Django/tango_with_django_project/rango* 目录下 `views.py` 代码

```
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):     # creat one view called index
    return HttpResponse("Rango says Tango with Django!") # 页面返回这一串字符
```

项目 *Tango-with-Django/tango_with_django_project/tango_with_django_project/ 目录下`urls.py` 代码:

```
from rango import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'), # ^$ 为正则表达式
    url(r'^admin/', admin.site.urls),
```

接下来运行app:

`[rango] PS E:\2016-for_Vocation\gopython\Tango-with-Django\tango_with_django_project> python manage.py runserver`

在浏览器中浏览地址:  http://127.0.0.1:8000
我们可以看到: 
![django-creating-view](https://dn-learnml.qbox.me/image/web/django-creating-view.JPG)

so 当我们打开 http://127.0.0.1:8000, url -- > views.index(index function in views.py) --> return HttpResponse("Rango says Tango with Django!") 就看到我们在上面看到的那样.
 
总结: 修改 *app* 文件目录下 `views.py` 有 *project* 文件目录下 的 `urls.py` 文件 如上, 我们就能在网页看到 `views.py` 下 index function http返回的内容(字符串"Rango says Tango with Django!").

## 3 Mapping urls

上面我们是在 `http://127.0.0.1:8000` 中查看 views.py 下 index function 返回的内容.

要是我们要想要在 `http://127.0.0.1:8000/rango/` 中查看相同的内容怎么办? 就是通过 **url 映射** 一一对应吧.

怎么一一对应? 

在 *project* 文件目录下 的 `urls.py` 添加 `url(r'^rango/', include('rango.urls'))`, 最后代码为,(参见 [:dancer: django rango mapping urls](https://github.com/JeremiahZhang/gopython/commit/539844b8c0494747f52d82180a3373dad1e7d452))

```
from django.conf.urls import url
from django.contrib import admin
from django.contrib import admin
from django.conf.urls import include

from rango import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^rango/', include('rango.urls')), # 添加url参数
    # above maps any URLs starting
    # with rango/ to be handled by
    # the rango application
    url(r'^admin/', admin.site.urls),
]
```

同时要在 *rango* app 应用目录的 `urls.py` [添加代码](https://github.com/JeremiahZhang/gopython/commit/539844b8c0494747f52d82180a3373dad1e7d452#diff-4b926fabdc64b0d52e0507666b230ee0)

```
from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```

我想逻辑是这样的:

- 当我们打开 `http://127.0.0.1:8000/rango/`
- 对应 *project* 下的 `urls.py` ---> 
- ---> `url(r'^rango/', include('rango.urls'))`
    - ---> `rango` 目录下的 `urls.py`
        - ---> `url(r'^$', views.index, name='index')`,
            - ---> rango app 下的 `views.py`
                - `def index` function
                    - `return`.

我们就看到下面的输出:  

![django-mapping-url-index](https://dn-learnml.qbox.me/image/web/django-mapping-url-index.JPG)

因此, 我们也可以建立一个 `about` 的页面：`http://127.0.0.1:8000/rango/about/` 参考[:dancer: django creat about page](https://github.com/JeremiahZhang/gopython/commit/293cd20c98a01b5fb367421b8a97a2fb84ee7fc3#diff-df5999a8b1cf17766efc47c447247a73)

输出为:

![django-mapping-url-about](https://dn-learnml.qbox.me/image/web/django-mapping-url-about.JPG)

---

# end

在使用`django-admin.py startproject [project_name]`建立项目后, 我们使用`python manage.py startapp rango` 建立 Django app 应用, 之后建立*views* 和 映射urls.

---

    @anifacc
    2017-04-18