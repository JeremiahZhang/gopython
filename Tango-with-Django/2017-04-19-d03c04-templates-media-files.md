# 4 Templates and Media Files

> In this chapter, we’ll be introducing the Django template engine, as well as showing how to serve both static files and media files, both of which can be integrated within your app’s webpages.

使用模板和媒体文件.

- 4.1 使用 templates
    - 动态路径设置 Dynamic Paths 
- 4.2 静态媒体文件提供
    - static media files and templates
- 4.3 Serving Media
- 4.4 基本流程

# 4.1 使用 templates

上一章的内容是webpage 建立 views 和 url 映射, 本章内容就设计到使用 templates, 让我们的 webpage 页面更加丰富些, 后面使用 css 的话 就是进行美化咯.

> Why Templates? The layout from page to page within a website is often the same.

为什么要使用 templates, 使用 templates 避免重复性.

建立 *templates* direcory 与 *rango* app *tango_with_django_project*在同一个directory 中.

修改 *tango_with_django_project* directory 中的 project's `settings.py`. 如[dynamic templates path](https://github.com/JeremiahZhang/gopython/commit/28763f556de6e818bfb50795901e0a52a0a38938)代码修改所示, 设置好 templates 的路径, 不要使用绝对路径, 而要使用动态路径, 这样无论在那台机子, 那个用户使用, 都可以正常使用.

关于对动态路径的理解, 可以直接查看代码[os.path tango test](https://github.com/JeremiahZhang/gopython/commit/c5acb8d6a3a06633c3dcee6734335a395b4b4c65)理解下.

*templates* 的动态路径设置好之后, 我们就可以添加 *templates* 模板, 比如我们添加 `index.html`, 并放入 *templates* directory 中. 

编辑 `index.html` 内容可参看[index.html](https://github.com/JeremiahZhang/gopython/commit/1fb568f00d32f0927c7c7682a045b316ecdf21bc#diff-b228ba07efe810cb1431bb792fc6f36d)

之后就要修改 *rango/views.py*, 如 [views.py](https://github.com/JeremiahZhang/gopython/commit/1fb568f00d32f0927c7c7682a045b316ecdf21bc#diff-b9677ab0168a9d9afbba0d0f2ecfdde5)

之后运行我们的 development server, 我们可以看到下面的截图:

![templates](https://dn-learnml.qbox.me/image/web/templates-index-html.JPG)

在这个小节中, 我们使用templates来展现我们的webpage, 比上一章直接返回字符串优雅很多.

主要就是:

- 添加 *templates* dir 动态路径 [:dancer: dynamic templates path · JeremiahZhang/gopython@28763f5](https://github.com/JeremiahZhang/gopython/commit/28763f556de6e818bfb50795901e0a52a0a38938)
- 在 *templates* dir 中添加我们要使用的 `html` 文件 并 修改*rango*应用下的`views.py`:[:dancer: add a template & check · JeremiahZhang/gopython@1fb568f](https://github.com/JeremiahZhang/gopython/commit/1fb568f00d32f0927c7c7682a045b316ecdf21bc)

# 4.2 提供静态媒体文件

我们知道如何使用 template 了, 那么如何在我们的页面web page中提供图片等静态媒体文件呢?

所谓静态媒体文件就是不是由web server 动态提供或产生的. 

还是与上一节类似, 

- 先建立 *static* directory(和 *templates* directory 在同一个目录下),并在其中建立 *images* directory, 将 *rango.jpg* 图片放入其中, 
- 然后修改同一目录下 project directory 中的 `settings.py` 配置对应的路径和URL.
- 修改 `index.html` 下内容

具体修改 可查看 [static server commit](https://github.com/JeremiahZhang/gopython/commit/312079e70756f1f2883dfa62c0ffceff5429412e#diff-7f6bb082d09de87fb7295328c94415d8)提交的代码.

运行我们的 development server, 可以看到如下效果:

![static-image](https://dn-learnml.qbox.me/image/web/static-image.JPG)

# 4.3 serving media

如果要使用用户上传的媒体文件比如 `cat.jpg` 图片该怎么办呢?

- 建立 *media* dir 与 *static* 在同一目录下, 假设我们的media是被upload到这个 *media* dir中的.
- 配置 project [setting.py](Tango-with-Django/tango_with_django_project/tango_with_django_project/settings.py )
- 修改 project [urls.py](https://github.com/JeremiahZhang/gopython/commit/1a454024e5dc1ac2a613213d60e7443506fbf404#diff-df5999a8b1cf17766efc47c447247a73)

运行我们的 development server, 在浏览器中的地址 `http://localhost:8000/media/cat.jpg` 查看效果, 如下图所示:

![media-file](https://dn-learnml.qbox.me/image/web/media-file.JPG)

代码提交: [:dancer: static media server](https://github.com/JeremiahZhang/gopython/commit/1a454024e5dc1ac2a613213d60e7443506fbf404)

# 4.4 基本流程

- 使用 templates
- 提供 static media
- 提供 media

# exercise 

> - Convert the about page to use a template as well, using a template called about.html.
> - Within the new about.html template, add a picture stored within your project’s 
static files.
> - On the about page, include a line that says, This tutorial has been put together
by <your-name>.
> - In your Django project directory, create a new directory called media, download a
picture of a cat and save it the media directory in a file called, cat.jpg.
> - In your about page, add in the <img> tag to display the picture of the cat, to ensurethat your media is being served correctly.

[code commit here]([:dancer: c4 exercise media img in about page · JeremiahZhang/gopython@abf2bbe](https://github.com/JeremiahZhang/gopython/commit/abf2bbe99b1b56836a9dba6709afcfa855ad06d1#diff-62d460ccc41fa3d05705285cc554ad4f))

主要是 `about.html` 中图片的连接问题.

```
<img src="/media/cat.jpg" alt="Cat img">
```

效果：

![about-media](https://dn-learnml.qbox.me/image/web/about-media.JPG)

---

    @anifacc
    2017-04-19