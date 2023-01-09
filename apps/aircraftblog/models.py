from django.db import models
import os
from django.utils.text import slugify
from django.utils.html import mark_safe
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext as _
from apps.users.profiles.models import Profile


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



class Post(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)


class Meta:
    abstract = True
    db_table = ''
    managed = True
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'


class Manufacturer(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    brand_logo = models.ImageField(upload_to='images/manufacturer_logos/')
    description = models.TextField()

    def __str__(self):
        return self.name

    @property
    def thumbnail_preview(self):
        if self.brand_logo:
            return mark_safe('<img src="{}" width="150" />'.format(self.brand_logo.url))
        return ""

def logo_directory_path(instance, filename):
        company_name = slugify(instance.brand)
        model_name = slugify(instance.model)
        family_name = slugify(instance.family)
        _, extension = os.path.splitext(filename)
        return f"Aircrafts/{company_name}/{model_name}-{family_name}{extension}"

class AircraftItem(Post):

      class ImageField(models.ImageField):
         def value_to_string(self, obj): # obj is Model instance, in this case, obj is 'Class'
            return obj.feature_img.url # not return self.url
      TYPE = (
        ("Passenger airplane", "Passenger airplane"),
        ("Freigther airplane", "Freigther airplane"),

      )
      BODY = (
        ("Wide body airplane", "wide_body"),
        ("Narrow body airplane", "narrow_body"),
      )
      category = TreeForeignKey('Category',null=True,blank=True, on_delete=models.CASCADE)
      feature_img = models.ImageField(upload_to=logo_directory_path, blank=True, null=True)
      type = models.CharField(_("Type"), choices=TYPE, max_length=50, blank=False)
      brand = models.ForeignKey(Manufacturer, verbose_name=_("Brand"), on_delete=models.CASCADE)
      model = models.CharField(_("Model"), max_length=20, default="")
      family = models.CharField(_("Family"), max_length=10, default="")
      bodytype = models.CharField(_("Body"), choices=BODY, max_length=50, blank=True, default="")
      base_model = models.CharField(_("Base model"), max_length=50, default="")
      tags = models.ManyToManyField(Tag, blank=True)


      def __str__(self):
        return f"{self.brand} + {self.model} + {self.family}"
    
