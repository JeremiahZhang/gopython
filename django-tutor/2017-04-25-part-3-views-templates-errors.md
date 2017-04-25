# Writing my first Django app part 3

接下来我们来到了 django 教程的第三部分, 这部分是使用 views 和 templates 来展示 app 的网页.

开始呢, 我们需要有一个大概的框架, 要清楚不同的页面`views`的作用是什么!在这个 `polls` 应用中, 有4个`views`, 如下:

> - Question “index” page – displays the latest few questions.
> - Question “detail” page – displays a question text, with no results but with a form to vote.
> - Question “results” page – displays results for a particular question
> - Vote action – handles voting for a particular choice in a particular question.

因此我们要清楚不同 views 的功能. 下面的 workflow 就是:

- 1 Writing more views
- 2 Raising a 404 error
- 3 Using the template system
- 4 Removing hardcoded URLs in templates

## 1 Writing more views

这里我们编辑 [`mysite/polls/views.py`](https://github.com/JeremiahZhang/gopython/commit/7035f2d51a88b06ae8e0b6b74d1ef22d574b6df5#diff-72cb325fea722b7dfb58fd8a5b3c1dd5)

```
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

使用 `HttpResponse` 来响应.

建立 views 后, 还需要修改 [`mysite/polls/urls.py`](https://github.com/JeremiahZhang/gopython/commit/7035f2d51a88b06ae8e0b6b74d1ef22d574b6df5#diff-df0f49bc766992e4c08dea8f8f45fab5)

```
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
```

可以看到, 不同的 views 对应不同 url. 在这里类似 `r'^(?P<question_id>[0-9]+)/$'` 使用了[正则表达式](https://docs.python.org/2.7/library/re.html#regular-expression-syntax).

对于不同的 url 分别可以看到不同的 views.

想要让 views 真正的显示也内容, `mysite/polls/views.py`就需要做一下编辑:

```
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

# Leave the rest of the views (detail, results, vote) unchanged
```

也就是将 models 中的 Question 数据库内容在这里显示一些.

然后要建立 `mysite/polls/templates/polls/index.html`,

- 先在 `mysite/polls/` 建立 `templates` directory, 这与 Tango with Django 教程不同, 在 polls app下直接建立的 templates. 不是在 `mysite` projects root directory 下建立的. 只需确认 `mysite/setting.py` 中 `TEMPLATE` 下的 `APP_DIRS': True`.
- 再在 `templates` directory 建立 `polls`
- 最后建立 `index.html` 文件并编辑如下

`/mysite/polls/templates/polls/index.html`:

```
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

在这里使用的是 Django 自身的 template system. 

`mysite/polls/views.py`:

```
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

也可以使用 shortcut: `render()` [shortcut render() · JeremiahZhang/gopython@6e548b3](https://github.com/JeremiahZhang/gopython/commit/6e548b3f5ae9b686affff27e242545cb8f753aca)

```
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```

效果是一样的.

---

## 2 [Raising a 404 error](https://docs.djangoproject.com/en/1.10/intro/tutorial03/#raising-a-404-error)

这个比较简单, 只要按照教程来就没问题.[http 404 raise · JeremiahZhang/gopython@c062c1c](https://github.com/JeremiahZhang/gopython/commit/c062c1ceae4f68e4a26f802cf450d17726f1d9c2)

推荐使用 `get_object_or_404`. [shortcut 404 · JeremiahZhang/gopython@bd39dac](https://github.com/JeremiahZhang/gopython/commit/bd39dac7473ba1ef79ae3db5f13aa98710d0c17a)

## 3 [Using the template system](https://docs.djangoproject.com/en/1.10/intro/tutorial03/#use-the-template-system)

[template system success · JeremiahZhang/gopython@bf585e6](https://github.com/JeremiahZhang/gopython/commit/bf585e61044b99399273082b3791029687fda4e2)

没有多大问题

## 4 [Removing hardcoded URLs in templates](https://docs.djangoproject.com/en/1.10/intro/tutorial03/#removing-hardcoded-urls-in-templates)

[removeing hardcoded URLs in templates · JeremiahZhang/gopython@89a2f66](https://github.com/JeremiahZhang/gopython/commit/89a2f66fd5777a248ac06838ffbb5c84fae8f472)

没有问题

[Namespacing URL names](https://docs.djangoproject.com/en/1.10/intro/tutorial03/#namespacing-url-names) 在一个项目下 多个应用 这个就有用啦

[namespacing URL names · JeremiahZhang/gopython@fd9bffd](https://github.com/JeremiahZhang/gopython/commit/fd9bffd98e8ac044d2f51786cc5933e5f52f7692)

---

# end 

这部分走下来, 正则表达式的理解是一方面, 基本理解.
另一方面是 templates 的使用, 不用 hardcoded templates, 在 templates html 文件如何修改对应的 url 值得注意.

---

```
@anifacc  
2017-04-25
```