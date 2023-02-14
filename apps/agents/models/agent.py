from django.db import models
from apps.profiles.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.utils.html import mark_safe

import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
from apps.agents.utils import unique_order_id_generator
from django.db.models.signals import pre_save
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Agent(models.Model):

    profile = models.OneToOneField(Profile, verbose_name=_(
        "profile_agent"), on_delete=models.CASCADE)
    agentid = models.CharField(max_length=15, null=True, blank=True)

    barcode = models.ImageField(upload_to='agents/barcodes/', blank=True)

    def __str__(self):
        return f"{self.agentid.upper()}"
        # return u"%s" % (self.profile)
    
    def get_agent_name(self):
        return f"{self.profile.first_name}-{self.profile.second_name}"
    
    def get_agent_phone(self):
        return f"{self.profile.phone}"

    def save(self, *args, **kwargs):          # overriding save() 
        COD128 = barcode.get_barcode_class('code128')
        rv = BytesIO()
        code = COD128(f'{self.agentid}', writer=ImageWriter()).write(rv)
        self.barcode.save(f'{self.profile.last_name}.png', File(rv), save=False)
        return super().save(*args, **kwargs)

    @property
    def barcode_preview(self):
        if self.barcode:
            return mark_safe('<img src="{}" width="150" />'.format(self.barcode.url))

    # @classmethod
    # def get_new(cls):
    #     return cls.objects.create().id



def pre_save_create_agentid(sender, instance, *args, **kwargs):
    if not instance.agentid:
        instance.agentid = unique_order_id_generator(instance)


pre_save.connect(pre_save_create_agentid, sender=Agent)
