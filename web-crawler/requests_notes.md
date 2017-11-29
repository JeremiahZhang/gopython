# requests modules learning

---

## 1. From the beginning

```
>>> import requests
>>> res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
>>> type(res)
<class 'requests.models.Response'>
>>> res.status_code == requests.codes.ok
True
>>> len(res.text)
174130
>>> print(res.text[:250])
ï»¿The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project
>>> help(requests)
Help on package requests:

NAME
    requests

DESCRIPTION
    Requests HTTP Library
    ~~~~~~~~~~~~~~~~~~~~~

    Requests is an HTTP library, written in Python, for human beings. Basic GET
    usage:

       >>> import requests
       >>> r = requests.get('https://www.python.org')
       >>> r.status_code
       200
       >>> 'Python is a programming language' in r.content
       True

    ... or POST:

       >>> payload = dict(key1='value1', key2='value2')
       >>> r = requests.post('http://httpbin.org/post', data=payload)
       >>> print(r.text)
       {
         ...
         "form": {
           "key2": "value2",
           "key1": "value1"
         },
         ...
       }

    The other HTTP methods are supported - see `requests.api`. Full documentation
    is at <http://python-requests.org>.

    :copyright: (c) 2017 by Kenneth Reitz.
    :license: Apache 2.0, see LICENSE for more details.

PACKAGE CONTENTS
    __version__
    _internal_utils
    adapters
    api
    auth
    certs
    compat
    cookies
    exceptions
    help
    hooks
    models
    packages
```

可直接用

```
>>> res.status_code == 200
True
```

查看 网页请求 是否成功。（‘OK’ in the HTTP protocol is 200）

## 2. raise error

```
>>> res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
>>> res.raise_for_status()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "D:\ProgramData\Anaconda2\envs\ten_years\lib\site-packages\requests\models.py", line 935, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: http://inventwithpython.com/page_that_does_not_exist
```

这就是程序停止. 如果不想其停止, 则使用 `try, except` 封装.

```
>>> try:
...     res.raise_for_status()
... except Exception as exc:
...     print('There was a problem: {}'.format(exc))
...
There was a problem: 404 Client Error: Not Found for url: http://inventwithpython.com/page_that_does_not_exist
>>>
```

总:

```
import requests
res = request.get('http://inventwithpython.com/page_that_does_not_exist')
try: 
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: {}'.format(exc))
```

> Always call raise_for_status() after calling requests.get(). You want to be sure that the download has actually worked before your program continues.

---

## 3.Saving downloaded files to the hard drive

```
>>> res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
>>> res.raise_for_status()
>>> playFile = open('RomeoAndJuliet.txt', 'wb')
>>> for chunk in res.iter_content(100000):
...     playFile.write(chunk)
...
100000
14688

>>> playFile.close()
```

> The write() method returns the number of bytes written to the file. In the previous example, there were 100,000 bytes in the first chunk, and the remaining part of the file needed only 14,688 bytes.

---

# reference

- [Automate the Boring Stuff with Python](http://automatetheboringstuff.com/chapter11/)