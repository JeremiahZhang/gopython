# Writing my 1st Django app part 4

## 1 write a simple form

我们现在来写 `polls/templates/polls/detail.html` templates, 让 template 包括 HTML `<form>` 元素.

```
<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
{% endfor %}
<input type="submit" value="Vote" />
</form>
```

[HTML Form Elements](https://www.w3schools.com/html/html_form_elements.asp)可以进一步了解 HTML `form` elements.

> The HTML <form> element defines a form that is used to collect user input:

输出的结果是这样的:

![detail html form element](https://dn-learnml.qbox.me/image/web/part-4-form-detail.JPG)

```
<form action="{% url 'polls:vote' question.id %}" method="post">
```

> Using method="post" (as opposed to method="get") is very important, because the act of submitting this form will alter data server-side. Whenever you create a form that alters data server-side, use method="post". This tip isn’t specific to Django; it’s just good Web development practice.

问: "post" 和 "get" 的区别??? see [forms - When should I use GET or POST method? What's the difference between them? - Stack Overflow](http://stackoverflow.com/questions/504947/when-should-i-use-get-or-post-method-whats-the-difference-between-them)

假如我选择`Not much`选项, 然后点击 `Vote` 按钮, 后面怎么处理 send 到 database 的信息呢? 这就要对应
`polls/views.py` 下 **vote()** function 功能:

```
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
# from django.http import Http404
from django.template import loader

from django.urls import reverse

from .models import Question
from .models import Choice

# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

> **request.POST** is a dictionary-like object that lets you access submitted data by key name.
`request.POST['choice']` 返回 被选择的选项的 ID 值.

接下来就是要看 '/polls/3/results/' 了. 我们忍让需要在 `polls/views.py` 编辑 `results` function.

```
from django.shortcuts import get_object_or_404, render


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
```

这样`vote()` function 返回 到 results url. 进入 'results.html' 页面.

`polls/templates/polls/results.html` 的内容:

```
<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```

下面一步步来,

- 点击 choice 选项 - 再 `Vote`

![part-4-form-detail-vote](https://dn-learnml.qbox.me/image/web/part-4-form-detail-vote.JPG)

- 显示 Vote 结果

![part-4-form-detail-vote-results](https://dn-learnml.qbox.me/image/web/part-4-form-detail-vote-results.JPG)

- Vote again 回到 detail 页面

![detail html form element](https://dn-learnml.qbox.me/image/web/part-4-form-detail.JPG)

over and over again.

---

## 2 Use Generic views: Less code is better

在上面我们的 `polls/views.py` 中 `index`, `detail`, `result` function 代码非常多, 如何可以用少量代码就能实现相同的功能:

> Amend URLconf

`polls/urls.py`:

```
from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
```

这里 `detail` 和 `results` 中的 `<qusetion_id>` 改为 `<pk>` 要不然会出错.

> Amend Views

接下来就是修改

`polls/views.py`

```
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.
```

这样就能实现相同和之前相同的功能啦.

# end

关于 database QuerySet 使用, 如上面的 `Question.objects.order_by()`等, 请参考[QuerySet API reference | Django documentation | Django](https://docs.djangoproject.com/en/1.11/ref/models/querysets/) 和 [Making queries | Django documentation | Django](https://docs.djangoproject.com/en/1.10/topics/db/queries/#limiting-querysets)

commit code: 

- [part 4 write a simple form · JeremiahZhang/gopython@abfcf27](https://github.com/JeremiahZhang/gopython/commit/abfcf27860fae7e477ae01b24bdd8a3be496ac06)
- [use generic views · JeremiahZhang/gopython@b4f7088](https://github.com/JeremiahZhang/gopython/commit/b4f70880c3cc0b4e71cfc759eb6f10cd27179063)


---

```
@anifacc
2017-04-26
```