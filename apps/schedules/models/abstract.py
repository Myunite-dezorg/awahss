from django.db import models
from apps.schedules.models.uuid import BaseUUID




class BaseSched(BaseUUID):
    createAt = models.DateTimeField(auto_now=True, auto_now_add=False)
    updateAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True