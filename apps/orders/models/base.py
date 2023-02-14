from django.db import models
from apps.agents.models import Agent
from apps.organizations.models import Organization

class AbstractOrder(models.Model):
    
    agent = models.ForeignKey(Agent, verbose_name=_("Agent Order"), related_name="agent_order", on_delete=models.CASCADE)
    company = models.ForeignKey(Organization, verbose_name=_("Order for company"), related_name="company_order", on_delete=models.CASCADE)
    create_at = models.DateTimeField(_("Created"), auto_now=False, editable=True)
    updated_at=models.DateTimeField(_("Updated"), auto_now_add=False, editable=True)


    class Meta:
        abstract = True
