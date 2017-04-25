# models[^1]

> A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

基本:

- model 是 Python 的一个类, [django.db.models.Model](https://docs.djangoproject.com/en/1.10/ref/models/instances/#django.db.models.Model)的子类
- model 的每个属性 代表 数据库的 field(字段).
- With all of this, Django gives you an automatically-generated database-access API; see [Making queries](https://docs.djangoproject.com/en/1.10/topics/db/queries/).

---

# first Django app part 2

> 1 database setup

- `mysite/settings.py`
- Run `python manage.py migrate`

```
The migrate command looks at the INSTALLED_APPS setting and creates any 
necessary database tables according to the database settings in your 
mysite/settings.py file and the database migrations shipped with the app 
```

> 2 creating models

- edit `polls/models.py`
- Activating models: `INSTALLED_APPS` settings in `settings.py` in mysite root directory.
- run `python manage.py makemigrations polls`
- run `python manage.py migrate`

```
> three-step guide to making model changes:

- change your models(in `models.py`)
- Run `python manage.py makemigrations` to **create** migrations for those changes
- Run `python manage.py migrate` to **apply** those changes to the database.
```

> 3 Playing with the API

run `python manage.py shell`

具体 设置 数据库内容, 存储数据 提取数据等 与数据库的交互吧参考:

- [Related objects reference | Django documentation | Django](https://docs.djangoproject.com/en/1.10/ref/models/relations/)  
- [Making queries | Django documentation | Django](https://docs.djangoproject.com/en/1.10/topics/db/queries/)

> 4 Introducing  Django Admin

run `python manage.py runserver`

modify `admin.py`

```
from django.contrib import admin

# Register your models here.

from .models import Question

admin.site.register(Question)
```

---

# end

All of the commits are [here](https://github.com/JeremiahZhang/gopython/commit/e05b8449c673bbbd936d4acc23c21c36cb95ec3e)

---

```
@anifacc
2017-04-25
```

---

[1]:    https://docs.djangoproject.com/en/1.10/topics/db/models/#module-django.db.models