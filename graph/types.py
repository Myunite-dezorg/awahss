import graphene
from graphene_django import DjangoObjectType
from apps.directory import models
from apps.users.models import CustomUser
from apps.users.profiles.models import Profile
from django.conf import settings
from apps.flight_schedule.schema import ScheduleType
from apps.flight_schedule.models import FlightTask, Tag, TaskAttachments, DocsCategory
from apps.payload.models import Payload

class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
       

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
    
    avatar = graphene.String()

    def resolve_avatar(self, info):
        if self.avatar and self.avatar.url:
            return info.context.build_absolute_uri(self.avatar.url)

        else:
            return None

class TaskAttachType(DjangoObjectType):
    class Meta:
        model = TaskAttachments

    file = graphene.String()

    def resolve_docs(self, info):
        if self.file and self.file.url:
            return info.context.build_absolute_uri(self.file.url)

        else:
            return None

class DocsCategoryType(DjangoObjectType):
    class Meta:
        model = DocsCategory


class TagType(DjangoObjectType):
    class Meta:
        model = Tag

class PayloadType(DjangoObjectType):
    class Meta:
        model = Payload


class ScheduleType(DjangoObjectType):
    class Meta:
        model = FlightTask


class AirlineType(DjangoObjectType):
    class Meta:
        model = models.Airline

    arl_logo = graphene.String()
    banner_img = graphene.String()

    # def resolve_arl_logo(self, info):
    #   return info.context.build_absolute_uri(self.arl_logo.url)

    def resolve_arl_logo(self, info):
        if self.arl_logo and self.arl_logo.url:
            return info.context.build_absolute_uri(self.arl_logo.url)

        else:
            return None
    def resolve_banner_img(self, info):
        if self.banner_img and self.banner_img.url:
            return info.context.build_absolute_uri(self.banner_img.url)

        else:
            return None


class RegistrationType(DjangoObjectType):
    class Meta:
        model = models.Register
    
    ac_photo = graphene.String()

    def resolve_ac_photo(self, info):
        if self.ac_photo and self.ac_photo.url:
            return info.context.build_absolute_uri(self.ac_photo.url)

        else:
            return None

class StationType(DjangoObjectType):
   class Meta:
      model = models.Station

   country_flag = graphene.String()

   def resolve_country_flag(self, info):
        if self.country_flag and self.country_flag.url:
            return info.context.build_absolute_uri(self.country_flag.url)

        else:
            return None
