四5章内容的 workflow

- Setting up your database:
  - With a new Django project, we should first tell Django about the database we intend to use.(i.e. configure **DATABASES** in `settings.py`)
  - We can also register any models in the `admin.py` module of our app to make them accessible via the admin interface
- Adding a model
  - 1 create our new model(s) in my Django app's `models.py` file
  - 2 Update `admin.py` to include and register our new model(s)
  - 3 Perform the migration `$ python manage.py makemigrations <app_name>`
  - 4 Apply the changes `$ python manage.py migrate`. This will create the *necessary infrastructure* within the database for our new model(s)
  - 5 Creat/edit our population script for our new model(s)

一般使用数据库, 我们都会想到 Structured Query Language(SQL) 其实我也不知道这是什么玩意儿, 猜测就是保存数据-提取数据作用, 我们可以从数据库中取得我们想要的数据.

> Querying an underlying data - which can store all sorts of data, such as our website's user details - is taken care of the **Object Relational Mapper(ORM)**. In essence, data stored within a database table can be encapsulated within a model.

> **A model is a Python object** that describes your database table’s data.Instead of directly working on the database via SQL, you only need to manipulate the corresponding Python model object.

使用 Django 我们可以通过 `model` 来实现数据存储或提取等功能咯.

---

# 5.1 需求: 大体实现内容

我们走到现在, 即将要进行 models 和 Database 相关实践, 我们有那些需求需要实现呢?

1. Rango: a web page directory - a site containing links to other websites.
2. Webpage categories
3. A category has it's name, a number of visits, and a number of likes.
4. A page refers to a category, has a title, URL and a number of views.

---

# 5.2 配置 DATABASES: Telling Django about Our Database

在建立 model 之前, 我们需要设置 Django 中的 database.

在 Django 1.10 中, `setting.py` 中的 **DATABASE** 变量自动创建而来. 如:

```
# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

可以看出默认的database是由 轻量化的 database engine, SQLite 驱动. 当让我们也可以使用其他 database engine. 

---

# 5.3 创建 Models

既然已经配置好 database, we create the two initial data models for the Rango App in `models.py` in *rango* app directory.

1. Category(models.Model)
2. Page(models.Model)

`models.py` 详细代码如下:

```
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    
    def __unicode__(self): # I use Python 2.x 对于 Python 3.x 使用 __str__(self)
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title
```

当我们建立一个 model, 比如 `Category`, we need to specify the list of fields and their associated types, along with any required or optional parameters.

[问题] 关于 fiels 和 types 根据具体内容到底如何定义呢? 这是一个问题, 我暂时对其还处于未知的状态. (最后集结到一起看最后结束能不能解决.)

[commit info](https://github.com/JeremiahZhang/gopython/commit/6c92a6815cc29b10b8e303274a78253a0085bab9#diff-ed3bd895d3a30d841a7ffe0e83d9d930)

---

# 5.4 Creating and Migrating the Database

我们定义好 `models.py`, 之后就让 Django 自己来工作: create the tables in the underlying database.

使用的工具: **migration tool** to help us set up and update the database reflect any changes to our models.

也就是说如果我们的 `models.py` 内容有变化, 我们就需要使用 migration tool 来进行设置.
这里我们添加了两个 models, so we need to use the migration tool to update the database.

## 5.4.1 setting up： initializing dabase

> Create the database and all the associated tables so that data can then be stored within it.

PS使用 `$ python manage.py migrate` details as described below, 

```
[rango] PS E:\2016-for_Vocation\gopython\Tango-with-Django\tango_with_django_project> python manage.py migrate 
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sessions.0001_initial... OK
```

书上说 当我执行命令后, 总的 Django 项目根目录中会有 `db.sqlite3` 的文件, 其实这个在没有执行上面命令,就已经有了. 当然我们还要检查一下到底有么有.

> 下面我们需要建立 a superuser 来管理数据库.

执行命令 `$ python manage.py createsuperuser`

```
[rango] PS E:\2016-for_Vocation\gopython\Tango-with-Django\tango_with_django_project> python manage.py createsuperuser
Username (leave blank to use 'we'): anifacc
Email address: zhangleisuda@gmail.com
Password:foxxxxxx24
Password (again):foxxxxxx24
Superuser created successfully.
```

这个超级用户 superuser 可以在之后进行登录进入 Django admin interface 管理接口中. 密码和地址都需要记住哦.

## 5.4.2 Creating and Updating Models/Tables

- 初始化并建立 database 完成  
- superuser 也建立完成  
- 接下来就是 creating and updating Models/Tables

`$ python manage.py makemigrations rango`

```
[rango] PS E:\2016-for_Vocation\gopython\Tango-with-Django\tango_with_django_project> python manage.py makemigrations rango
Migrations for 'rango':
  rango\migrations\0001_initial.py:
    - Create model Category
    - Create model Page
```

After, we need to check the **rango/migrations** directory to see that a Python script has been created. 

It's `0001_initial.py`. details in [this commit link](https://github.com/JeremiahZhang/gopython/commit/6c92a6815cc29b10b8e303274a78253a0085bab9#diff-912d985cac76f20ec3f10e12add51a86)

> checking the underling SQL (optional) 非必需

`$ python manage.py sqlmigrate rango 0001

```
[rango] PS E:\2016-for_Vocation\gopython\Tango-with-Django\tango_with_django_project> python manage.py sqlmigrate rango 0001
BEGIN;
--
-- Create model Category
--
CREATE TABLE "rango_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(128) NOT NULL UNIQUE);
--
-- Create model Page
--
CREATE TABLE "rango_page" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(128) NOT NULL, "url" varchar(200) NOT NULL, "views" in
teger NOT NULL, "category_id" integer NOT NULL REFERENCES "rango_category" ("id"));
CREATE INDEX "rango_page_b583a629" ON "rango_page" ("category_id");
COMMIT;
```

> 我们的app 建立 migrations 后, 需要 commit them to the database:

`$ python manage.py migrate`

```
[rango] PS E:\2016-for_Vocation\gopython\Tango-with-Django\tango_with_django_project> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, rango, sessions
Running migrations:
  Applying rango.0001_initial... OK
```

成功.

---

# 5.5 Django Models and the Shell

`$ python manage.py shell`

进入 shell, interact with Django models directly from the Django shell.

---

# 5.6  Configuring the Admin Interface

配置 管理 接口啦

`$ python manage.py runserver`

浏览器进入 http://127.0.0.1:8000/admin/ 会呈现 一个 登录页面. 填入上面 superuser 的用户名和密码就可以进入啦.

Here I met a problem, similar like this question --- [python - Cannot run Django development server (UnicodeDecodeError) - Stack Overflow](http://stackoverflow.com/questions/28194803/cannot-run-django-development-server-unicodedecodeerror/43578889#43578889).

When I first ran it， it was ok. But after that, I ran another day it had the problem. So I changed the system locale from Chinese to English.

So we can see this below:

![admin superuser](https://dn-learnml.qbox.me/image/web/admin-superuser.JPG)

> But we are missing the *Category* and *Page* models that were defined for Rango app. To include these models like below:

![admin models](https://dn-learnml.qbox.me/image/web/admin-models.JPG)

we need to change the file `rango/admin.py` to *register* each class we want to include.

```
from django.contrib import admin

# Register your models here.

from rango.models import Category, Page

admin.site.register(Category)
admin.site.register(Page)
```

# 5.7 creating a population script

> Entering test data into your database tends to be a hassle. Many developers will add in some bogus test data by randomly hitting keys, like wTFzmN00bz7. Rather than do this, it is better to write a script to automatically populate the database with realistic and credible data. 

> - This is because when you go to demo or test your app, you’ll see some good examples in the database.   
> -Also, if you are deploying the app or sharing it with collaborators, then you/they won’t have to go through the process of putting in sample data. It’s therefore good practice to create what we call *a population script*.

So I create `Tango-with-Django/tango_with_django_project/populate_rango.py`, details in [commit](https://github.com/JeremiahZhang/gopython/commit/6c92a6815cc29b10b8e303274a78253a0085bab9#diff-687b885ea3821402a70a50849394fe0a)

Then do like this:

`$ python populate_rango.py`

Next we will see:

![populate-rango](https://dn-learnml.qbox.me/image/web/populate-rango.JPG)

---

# End

- Rango's requirement
- Telling Django about my Database
- creating models
- creating and migrating the database
- django models and the shell
- configuring the admin interface
- creating a population script

---

```
@anifacc
2017-04-24
```