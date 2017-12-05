# overview

- have the models set up
- populated the database with some sample data
- connecting models, views, templates to serve up dynamic content.

# Workflow data driven page

- From models import ... In `views.py`
- In `views.py` query the model to get the data you want to present.
- Then pass the results from your model into the template's context.
- Creat/Modify the template so that it displays the data from the context.
- Map a URL to your view.

## 主页显示目录 Categories

效果图 ![categories listed in homepage](https://dn-learnml.qbox.me/image/web/list-index-page.JPG)

代码: ['list-categories-in-index-page' · JeremiahZhang/gopython@245a15f](https://github.com/JeremiahZhang/gopython/commit/245a15f45bfaa2f334c37e30c45c29dbb88ea141)

## Update Category Table with a Slug Field

['slug-first-demoe' · JeremiahZhang/gopython@7d2f7cc](https://github.com/JeremiahZhang/gopython/commit/7d2f7cc42279607b958155ef5c08c6b80d01500b)

代码如上 之后:

```
python manage.py makemigrations rango
python manage.py migrate
```

![slug-first-demo](https://dn-learnml.qbox.me/image/web/slug-first-demo.JPG)

['slug-allows-blank-entries' · JeremiahZhang/gopython@f8268c2](https://github.com/JeremiahZhang/gopython/commit/f8268c2580b883b7ac973a7cf1217b4be2c6429c)

['auto-add-slug-field' · JeremiahZhang/gopython@a87c8e4](https://github.com/JeremiahZhang/gopython/commit/a87c8e4902132cceb136ce96794c48745ddb4ed4)
![auto-add-slug-field](https://dn-learnml.qbox.me/image/web/auto-add-slug-field.JPG)

['category-page-details' · JeremiahZhang/gopython@354e8ad](https://github.com/JeremiahZhang/gopython/commit/354e8ad126afeef01f441eef07cd8465c5c83893)

![category-link-index](https://dn-learnml.qbox.me/image/web/category-link-index.JPG)

['page-views-edit' · JeremiahZhang/gopython@d0bd3c0](https://github.com/JeremiahZhang/gopython/commit/d0bd3c0697073ec8918c463e4edafebec1ed219f)

![categories-detail](https://dn-learnml.qbox.me/image/web/categories-detail.JPG)


# exercises

![c6-exercise-demo](https://dn-learnml.qbox.me/image/web/c6-exercise-demo.JPG)

代码: ['c6-exercise' · JeremiahZhang/gopython@a2bc709](https://github.com/JeremiahZhang/gopython/commit/a2bc70962aa2324f02129f03b5b668a04badf5f9)

---

```
@anifacc  
2017-05-03
```