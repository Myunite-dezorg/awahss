from django.db import models
from .uuid import BaseUUID
from django.utils.translation import gettext_lazy as _



class DgrBase(BaseUUID): 

    dgr_class = models.IntegerField(_("Class"))
    description = models.TextField(_("Description"))

    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True