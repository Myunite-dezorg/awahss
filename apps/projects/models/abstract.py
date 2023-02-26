from django.db import models
import uuid

class UUID(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class Abstract(UUID):
    create_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    update_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True