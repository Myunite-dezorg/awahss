from django.db import models

class Payload(models.Model):
    PAY_TYPE = (
        ('cargo', 'cargo'),
        ('mail', 'mail'),
        ('equipments', 'equipments')
    )

    title = models.CharField("Payload title", max_length=255)
    type = models.CharField(choices= PAY_TYPE, max_length=50, default="cargo")
    messages = models.TextField()
    createAt = models.DateTimeField(auto_now=True, auto_now_add=False)
    updateAt = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.type}"

