from django.db import models
import os
from django.utils.text import slugify
from django.utils.html import mark_safe
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext as _
from apps.profiles.models import Profile
from taggit.managers import TaggableManager


class Category(MPTTModel):
  name = models.CharField(max_length=50, unique=True)
  parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)
  slug = models.SlugField()

  class MPTTMeta:
    order_insertion_by = ['name']

  class Meta:
    unique_together = (('parent', 'slug',))
    verbose_name_plural = 'categories'

  def get_slug_list(self):
    try:
      ancestors = self.get_ancestors(include_self=True)
    except:
      ancestors = []
    else:
      ancestors = [ i.slug for i in ancestors]
    slugs = []
    for i in range(len(ancestors)):
      slugs.append('/'.join(ancestors[:i+1]))
    return slugs

  def __str__(self):
    return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



class Article(models.Model):

    class ImageField(models.ImageField):
         def value_to_string(self, obj): # obj is Model instance, in this case, obj is 'Class'
            return obj.feature_img.url # not return self.url
    class Meta:
        ordering = ["-publish_date"]

    category = models.ForeignKey(Category, verbose_name=_("Articles_category"), on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    feature_img = models.ImageField(upload_to="articles/%m-%d-%Y/", blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = TaggableManager()

    def get_owner_pp(self):
        return self.author.avatar.url
    def get_feature_img(self):
      return self.feature_img.url


    @property
    def feature_thumbnail_preview(self):
        if self.feature_img:
            return mark_safe('<img src="{}" width="150" />'.format(self.feature_img.url))
        return ""


class Meta:
    abstract = True
    db_table = ''
    managed = True
    verbose_name = 'Article'
    verbose_name_plural = 'Articles'

    def __str__(self):
        return f"{self.title} - {self.author}"

