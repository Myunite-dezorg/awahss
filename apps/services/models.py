from django.db import models
import enum
import logging
from apps.users.models import User
from django.conf import settings
from apps.agents.models import Agent
from django.utils.translation import gettext_lazy as _
from apps.services.uuid import BaseUUID
from apps.agents.models import Agent
from apps.stuffs.models import Aog
from django.shortcuts import reverse
from apps.schedules.models import RegularScheduler
from core.utils.mail import send_mail_async as send_mail
from hashlib import sha1
# from django.http import HttpResponseRedirect
# from django.http import FileResponse
# import io
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter

logger = logging.getLogger(__name__)

number_tr = _("number")




TASK_PRIORITY_FIELDS = ('-type', )

class State(enum.Enum):
    """
    Status of completion of the task
    (codes are prefixed with numbers to be easily sorted in the DB).
    """
    TO_DO = '00-to-do'
    IN_PROGRESS = '10-in-progress'
    DONE = '30-done'
    DISMISSED = '40-dismissed'

class Type(enum.Enum):
    """
    The priority of the task
    (codes are prefixed with numbers to be easily sorted in the DB).
    """
    ONLOAD = '00-onload'
    OFFLOAD = '10-offload'
  

class ServiceManager(models.Manager):

    def others(self, pk, **kwargs):
        """
        Return queryset with all objects
        excluding the one with the "pk" passed, but
        applying the filters passed in "kwargs".
        """
        return self.exclude(pk=pk).filter(**kwargs)

class BaseServiceRequest(BaseUUID):

    STATES = (
        (State.TO_DO.value, _('To Do')),
        (State.IN_PROGRESS.value, _('In Progress')),
        (State.DONE.value, _('Done')),
        (State.DISMISSED.value, _('Dismissed'))
    )
    TYPES = (
        (Type.ONLOAD.value, _('Onload')),
        (Type.OFFLOAD.value, _('Offload')),
    )

    type = models.CharField(_("type"), max_length=20, choices=TYPES, default=Type.OFFLOAD.value)
    data_createAt = models.DateTimeField(
        _("DateTime created"), auto_now=True, editable=False)
    data_updateAt = models.DateTimeField(
        _("DateTime updated"), auto_now=False, auto_now_add=True, editable=False)

    # agent = name = models.ForeignKey(
    #     Agent, related_name='agent_service_request', on_delete=models.CASCADE)
    request_date = models.DateField(
        _("Service date"), auto_now=True)
    
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='users_created', verbose_name=_('created by'),
    #                                on_delete=models.SET_NULL, null=True)

    objects = ServiceManager()

    class Meta:
        abstract = True


class AogService(BaseServiceRequest):

    # agent = models.ForeignKey(
    #     Agent, related_name='agent_services_request', on_delete=models.CASCADE)
    # service_item = models.ManyToManyField(
    #     Aog, related_name="aog_service_items")
   
    service_name = models.CharField(
        _("Service name"), max_length=50, blank=False, null=False)
    flight = models.ForeignKey(RegularScheduler, related_name="aog_from_flight", on_delete=models.CASCADE)

    aog_item = models.ManyToManyField(Aog)
    fix_required = models.BooleanField(_("Fix on board"), default=False)
  
    responsibles_persons = models.ManyToManyField(
        'DutyPerson')
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(Agent, related_name='agent_created', verbose_name=_('created by'),
                                   on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return "[%s] %s" % (self.number, self.flight)

    @property
    def number(self) -> str:
        return "{:08d}".format(self.pk)

    # def __str__(self):
    #     return f" {self.service_name} / {self.service_date} | {self.flight} | {self.agent}"


    def get_absolute_url(self):
        return reverse("AogService", kwargs={"pk": self.pk})



    class Meta:
        indexes = [
            models.Index(fields=TASK_PRIORITY_FIELDS, name='service_priority_idx'),
        ]


class DutyPerson(BaseUUID):

    class Meta:
        verbose_name = _("Responsble person")
        verbose_name_plural = _("Responsibles")


    service = models.ForeignKey(AogService, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, verbose_name=_("Users persons stuff"), on_delete=models.CASCADE)
    full_name = models.CharField(_("Full Name"), max_length=50)
    position = models.CharField(_("Person position"), max_length=50)
    contact_phone = models.CharField(_("Contact Phone"), max_length=12)

    def __str__(self):
        return self.full_name
