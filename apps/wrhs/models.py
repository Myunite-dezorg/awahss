from django.db import models
from .dgrbase import DgrBase
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.utils.html import mark_safe
from mptt.models import MPTTModel, TreeForeignKey
from apps.wrhs.base_directory.models import ImpCode

class DCategory(MPTTModel):
    category_name = models.CharField(_("Category name"), max_length=50)
    description = models.TextField(null=True, blank=True)
    parent = TreeForeignKey('self', verbose_name="Subdivision", on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField()

    class MPTTMeta:
      order_insertion_by = ['category_name']

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
        return self.category_name

class DGRClass(DgrBase):
    category = models.ForeignKey(DCategory, related_name="dgr_category", on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=50)
    imp_code = models.CharField(_("Imp code1"), default='...', max_length=3)
    imp_code2 = models.CharField(_("Imp code2"), default='', max_length=3)
    imp_code3 = models.CharField(_("Imp code3"), default='', max_length=3)
    # imp_code2 = models.ForeignKey(ImpCode, verbose_name=_("drg_imp_code2"), on_delete=models.CASCADE)
    # imp_code3 = models.ForeignKey(ImpCode, verbose_name=_("drg_imp_code3"), on_delete=models.CASCADE)
   
    cao = models.BooleanField(_("CAO"),  default=False)
    dgr_label = models.ImageField(_("Label"), upload_to="wrh/dgr/labels/", null=True)
    remarks = models.TextField(null=True)


    def __str__(self):
        return f"{self.imp_code1}-{self.name}"

    @property
    def label_preview(self):
        if self.dgr_label:
            return mark_safe('<img src="{}" width="80" />'.format(self.dgr_label.url))
        return ""
