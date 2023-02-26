import graphene
from .types import *
from apps.directory import models
from apps.users.models import CustomUser
from apps.users.profiles.models import Profile
from django.conf import settings
from apps.projects.schema import ScheduleType
from apps.projects.models import FlightTask, Tag, TaskAttachments, DocsCategory
from apps.payload.models import Payload




class Query(graphene.ObjectType):
    get_user_profile = graphene.List(ProfileType)
    get_users = graphene.List(UserType)
    all_airlines = graphene.List(AirlineType)
    get_registers = graphene.List(RegistrationType)
    all_flights = graphene.List(ScheduleType)
    get_taskTags = graphene.List(TagType)
    get_stations = graphene.List(StationType)
    get_payload = graphene.List(PayloadType)
    get_flights_task_docs = graphene.List(TaskAttachType)

    # JKNK------>>>>
    get_task_by_id = graphene.Field(ScheduleType, pkid=graphene.String())

    def resolve_get_users(root, info):
        return (
            CustomUser.objects.all()
        )
    def resolve_get_user_profile(root, info):
        return (
            Profile.objects.all()
        )
    def resolve_all_airlines(root, info):
        return (
            models.Airline.objects.all()
        )

    def resolve_get_registers(root, info):
        return (
            models.Register.objects.all()
        )
    def resolve_all_flights(root, info):
        return (
            FlightTask.objects.all()
        )
    def resolve_get_stations(root, info):
        return (
            models.Station.objects.all()
        )
    def resolve_get_payload(root, info):
        return (
            Payload.objects.all()
        )
    def resolve_get_taskTags(root, info):
        return (
            Tag.objects.all()
        )
    def resolve_get_flights_task_docs(root, info):
        return (
            TaskAttachments.objects.all()
        )

    def resolve_get_task_by_id(root, info, pkid):
        return (
            FlightTask.objects.get(pk=pkid)
        )
