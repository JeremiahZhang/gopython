from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible

from django.template.defaultfilters import slugify

# Create your models here.

@python_2_unicode_compatible # only if you need to support Python 2
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self): 
        return self.name

@python_2_unicode_compatible
class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title