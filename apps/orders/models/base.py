from django.db import models
from apps.agents.models.agent import Agent
from apps.agents.models.company import Company

from django.utils.translation import gettext as _

class AbstractOrder(models.Model):
    
    agent = models.ForeignKey(Agent, verbose_name=_("Agent Order"), related_name="agent_order", on_delete=models.CASCADE)
    company = models.ForeignKey(Company, verbose_name=_("Company order"), related_name="company_order", on_delete=models.CASCADE)
    create_at = models.DateTimeField(_("Created"), auto_now=True, editable=True)
    updated_at=models.DateTimeField(_("Updated"), auto_now_add=True, editable=True)


    class Meta:
        abstract = True
