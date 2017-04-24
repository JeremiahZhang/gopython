# 3.2 创建 django 项目

本节内容是创建 django 项目, 并在浏览器中简单显示。我们一步步来.

因为我们已经配置好系统环境了, 之前我们使用的 conda 来进行配置的.

打开PS, 通过

`$ activate rango` 

进入 rango 环境下.

进入到我们的工作空间（文件夹）下, 比如我工作空间（文件夹）是*E:\2016-for_Vocation\gopython\Tango-with-Django*, 我就在PS中打开到我们的工作空间（文件夹）.具体可观察下面代码及提示（注: > 后面才是我们要输入的代码）

    [rango] PS E:\2016-for_Vocation\gopython\Tango-with-Django> django-admin.py startproject tango_with_django_project

主要是键入: `$ django-admin.py startproject tango_with_django_project` 执行 ` django-admin.py` 程序, 我们在当前文件下创建 *tango_with_django_project* 文件夹, 通过`ls`我们可以查看:

```
[rango] PS E:\2016-for_Vocation\gopython\Tango-with-Django> ls


    目录: E:\2016-for_Vocation\gopython\Tango-with-Django


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        2017/4/17     15:16                tango_with_django_project
-a----        2017/4/17     15:12          10068 TwD-D01-system-setup.md
```

我们可以发现上面的 *tango_with_django_project* 下还有一个 *tango_with_django_project*文件夹 和 *manage.py* 脚本.

大体目录树是这样的:

```
+ tango_with_django_project
    - tango_with_django_project
        + __init__.py # 空脚本, 它的存在为了表明当前这个directiory目录是 Python 包.
        + settings.py # 该脚本用来存储我们 Django 项目的所有设置
        + urls.py     # 该脚本用来存储我们的项目中的URL patterns(模式)
        + wsgi.py     # 该脚本帮助我们运行我们的开发服务器和在production env环境中不熟我们的项目
    - manage.py
```

进入 *tango_with_django_project* dir, 运行 *manage.py*, 如下：


`$ cd .\tango_with_django_project\`  # 先要打开 *tango_with_django_project* dir

然后

`$ python manage.py help` # 查看所有 command 命令

输出是:
```
Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
```

可以看到 *manage.py* 下的可以使用的命令.

下面我们就来使用下 `runserver` 命令

`$ python manage.py runserver`

outputs:

```
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin,
 auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
April 17, 2017 - 15:28:48
Django version 1.10.5, using settings 'tango_with_django_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

接下来我们在浏览器中打开 url **http://127.0.0.1:8000/**, 可以看到:

![web page intro](https://dn-learnml.qbox.me/image/web/web-django-c03-02-webpage.JPG)

也就是说, 当我们写好程序之后, runserver 一下, 就可以看到我们设计的web网页是怎么样的了, 在本地 localhost 浏览查看, 以便debug.

---

# end

和之前用*bottle* 类似, 道理是相同哒.

    @anifacc
    2017-04-17