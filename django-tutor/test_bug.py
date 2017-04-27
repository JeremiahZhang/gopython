# Identify bugs

"""
>>> import datetime
>>> from django.utils import timezone
>>> from polls.models import Question
>>> # create a Question instance with pub_date 30 days in the future
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
>>> future_question.was_published_recently()
True
"""

## Running a test

"""
[rango] PS E:\2016-for_Vocation\gopython\django-tutor\mysite> python manage.py test polls
Creating test database for alias 'default'...
F
======================================================================
FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionMethodTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "E:\2016-for_Vocation\gopython\django-tutor\mysite\polls\tests.py", line 19, in test_was_published_recently_with_
future_question
    self.assertIs(future_question.was_published_recently(), False)
AssertionError: True is not False

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
Destroying test database for alias 'default'...
"""

## Fix bugs 

"""
[rango] PS E:\2016-for_Vocation\gopython\django-tutor\mysite> python manage.py test polls
Creating test database for alias 'default'...
F
======================================================================
FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionMethodTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "E:\2016-for_Vocation\gopython\django-tutor\mysite\polls\tests.py", line 19, in test_was_published_recently_with_
future_question
    self.assertIs(future_question.was_published_recently(), False)
AssertionError: True is not False

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
Destroying test database for alias 'default'...
[rango] PS E:\2016-for_Vocation\gopython\django-tutor\mysite> python manage.py test polls
Creating test database for alias 'default'...
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
Destroying test database for alias 'default'...
"""

## More test

"""
[rango] PS E:\2016-for_Vocation\gopython\django-tutor\mysite> python manage.py test polls
Creating test database for alias 'default'...
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
Destroying test database for alias 'default'...
"""

# Test a View

"""
[rango] PS E:\2016-for_Vocation\gopython\django-tutor\mysite> python manage.py shell
Python 2.7.13 |Continuum Analytics, Inc.| (default, Dec 19 2016, 13:29:36) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.test.utils import setup_test_environment
>>> from django.test import Client
>>> # create an instance of the client for our use
>>> client = Client()
>>> # get a response from '/'
>>> response = client.get('/')
Invalid HTTP_HOST header: 'testserver'. You may need to add u'testserver' to ALLOWED_HOSTS.
>>> # we should expect a 404 from that address
>>> response.status_code
400
>>> response = client.get('/')
Invalid HTTP_HOST header: 'testserver'. You may need to add u'testserver' to ALLOWED_HOSTS.
>>> response.status_code
400
>>> # here leaver and error
>>> from django.urls import reverse
>>> response = client.get(reverse('polls:index'))
Invalid HTTP_HOST header: 'testserver'. You may need to add u'testserver' to ALLOWED_HOSTS.
>>> response.status_code
400
"""

"""
# ALLOWED_HOSTS = ['*'] fixed

>>> from django.test import Client
>>> client = Client()
>>> response = client.get('/')
Not Found: /
>>> response.status_code
404
"""

"""
>>> from django.urls import reverse
>>> response = client.get(reverse('polls:index'))
>>> response.status_code
200
>>> response.content
'\n    <ul>\n    \n        <li><a href="/polls/1/">what&#39;s new?</a>\n        </li>\n    \n    </ul>\n'
>>> response.context['latest_question_list']
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: 'NoneType' object has no attribute '__getitem__'
"""

"""
[rango] PS E:\2016-for_Vocation\gopython\django-tutor\mysite> python manage.py test polls
Creating test database for alias 'default'...
.....F.F.F
======================================================================
FAIL: test_index_view_with_a_future_question (polls.tests.QuestionViewTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "E:\2016-for_Vocation\gopython\django-tutor\mysite\polls\tests.py", line 78, in test_index_view_with_a_future_que
stion
    self.assertContains(response, "No polls are available.")
  File "D:\ProgramData\Anaconda2\envs\rango\lib\site-packages\django\test\testcases.py", line 382, in assertContains
    self.assertTrue(real_count != 0, msg_prefix + "Couldn't find %s in response" % text_repr)
AssertionError: Couldn't find 'No polls are available.' in response

======================================================================
FAIL: test_index_view_with_future_question_and_past_question (polls.tests.QuestionViewTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "E:\2016-for_Vocation\gopython\django-tutor\mysite\polls\tests.py", line 91, in test_index_view_with_future_quest
ion_and_past_question
    ['<Question: Past question.>']
  File "D:\ProgramData\Anaconda2\envs\rango\lib\site-packages\django\test\testcases.py", line 955, in assertQuerysetEqua
l
    return self.assertEqual(list(items), values, msg=msg)
AssertionError: Lists differ: ['<Question: Future question.>... != ['<Question: Past question.>']

First differing element 0:
'<Question: Future question.>'
'<Question: Past question.>'

First list contains 1 additional elements.
First extra element 1:
'<Question: Past question.>'

- ['<Question: Future question.>', '<Question: Past question.>']
+ ['<Question: Past question.>']

======================================================================
FAIL: test_index_view_with_two_past_questions (polls.tests.QuestionViewTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "E:\2016-for_Vocation\gopython\django-tutor\mysite\polls\tests.py", line 103, in test_index_view_with_two_past_qu
estions
    ['<Question: Past question 2.>', '<Queston: Past question 1.>']
  File "D:\ProgramData\Anaconda2\envs\rango\lib\site-packages\django\test\testcases.py", line 955, in assertQuerysetEqua
l
    return self.assertEqual(list(items), values, msg=msg)
AssertionError: Lists differ: ['<Question: Past question 2.>... != ['<Question: Past question 2.>...

First differing element 1:
'<Question: Past question 1.>'
'<Queston: Past question 1.>'

- ['<Question: Past question 2.>', '<Question: Past question 1.>']
?                                         -

+ ['<Question: Past question 2.>', '<Queston: Past question 1.>']

----------------------------------------------------------------------
Ran 10 tests in 0.090s

FAILED (failures=3)
Destroying test database for alias 'default'...
"""