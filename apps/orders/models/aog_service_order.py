from .base import AbstractOrder
from apps.agents.models.agent import Agent
from django.utils.translation import gettext as _
from django.db import models, transaction
from django.utils import timezone

class AogOrder(AbstractOrder):
    order_number = models.CharField(max_length=20, unique=True, editable=False)
    

    def save(self, *args, **kwargs):
        if not self.id:
            now = timezone.now()
            month = str(now.month).zfill(2)
            year = str(now.year)[-2:]
            with transaction.atomic():
                last_order = AogOrder.objects.select_for_update().order_by('-order_number').first()
                if last_order:
                    last_order_number = int(last_order.order_number[:6])
                else:
                    last_order_number = 0
                new_order_number = f"{str(last_order_number + 1).zfill(6)}-{month}-{year}"
                self.order_number = new_order_number
                super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def get_agent_id(self):
        return f"{self.agent.agentid}"

    def get_model_fields(agent):
        return agent._meta.get_field('agent')

    def __str__(self):
        return f"[{self.agent}]-{self.order_number}"

