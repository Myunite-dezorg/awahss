from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.



class ImpCode(models.Model):

    IMP_CHOICES_CAT = (
        ("SITA MESSAGE_CARGO", "SITA MESSAGE_CARGO"),
        ("TRANSPORT MESSAGES", "TRANSPORT MESSAGES"),
        ("COMMERCIAL MESSAGES", "COMMERCIAL MESSAGES"),
        ("IATA_CARGO_IMP_SUPPORT", "IATA_CARGO_IMP_SUPPORT"),
        ("IATA_PADIS_SUPPORT", "IATA_PADIS_SUPPORT"),
        ("SPECIAL HANDLING CODES", "SPECIAL HANDLING CODES"),
        ("DGR IMP CODES", "DGR IMP CODES"),


    )


    type = models.CharField(_("Type"), choices=IMP_CHOICES_CAT, max_length=60)
    code = models.CharField(_("Type"), max_length=7)
    description = models.CharField(_("Description"), max_length=255, default="")

    

    def __str__(self):
        return f"{self.code}-{self.description}"