# basic workflow 

第三章走下来, 整一个流程是这样的:

- 建立新的 Django project `python django-admin.py startproject <name>`
- 建立 application
    - ` python manage.py startapp <appname>`
    - project 下`settings.py` 增加 appname 到 INSTALLED_APPS 元组中
    - project 下`urls.py` 增加 application 应用的映射
    - app 下的`urls.py` 建立 URL 连接到 views
    - app 下`views.py` 建立url对应的 http response 响应

exercise：

- index 页面添加 about 页面连接
- about 页面添加 index 页面连接

完成内容参考 [:dancer: index in about page & viceverse](https://github.com/JeremiahZhang/gopython/commit/830cbd0f1d31a31f0c9dc2217229fd22f5f6e21b)

主要使用html.

具体文档参考 [Writing views | Django documentation | Django](https://docs.djangoproject.com/en/1.10/topics/http/views/)

# end

本章是Django 入门练习吧, 主要是设置虚拟环境比较折腾, 我是直接使用 conda 来进行虚拟环境设置的.

之后的主要内容就是: django basic workflow

---

    @anifacc