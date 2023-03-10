from django.db import models
from .uuid import BaseUUID
from django.utils.translation import gettext_lazy as _


class BaseSched(BaseUUID):
    createAt = models.DateTimeField(auto_now=True, auto_now_add=False)
    updateAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class RegularScheduler(BaseSched):
    tech_rout = models.CharField(_("Tech"), max_length=15)
    flt_number = models.CharField(_("Flight number"), max_length=8)
    airport = models.CharField(_("Airport"), max_length=3)
    sta = models.TimeField(_("STA"), null=True, blank=True)
    pta = models.TimeField(_("PTA"), null=True, blank=True)
    ata = models.TimeField(_("ATA"), null=True, blank=True)
    std = models.TimeField(_("STD"), null=True, blank=True)
    ptd = models.TimeField(_("PTD"), null=True, blank=True)
    atd = models.TimeField(_("ATD"), null=True, blank=True)



    def __str__(self):
        return u"%s" % (self.flt_number)
