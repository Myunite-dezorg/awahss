from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
import graphene

from apps.projects.models.flight_project import FlightProject


class ScheduleType(DjangoObjectType):
    class Meta:
        model = FlightProject


# class AuthorType(DjangoObjectType):
#     class Meta:
#         model = Profile

# class ProfileType(DjangoObjectType):
#     class Meta:
#         model = Profile

#     avatar = graphene.String()

#     def resolve_avatar(self, info):

#         return info.context.build_absolute_uri(self.avatar.url)

# class PostType(DjangoObjectType):

#     class Meta:
#         model = models.AircraftPost

#     feature_img = graphene.String()

#     def resolve_feature_img(self, info):

#         return info.context.build_absolute_uri(self.feature_img.url)


# class TagType(DjangoObjectType):
#     class Meta:
#         model = models.Tag


# class BrandType(DjangoObjectType):
#     class Meta:
#         model = models.Manufacturer

#     brand_logo = graphene.String()

#     def resolve_brand_logo(self, info):

#         return info.context.build_absolute_uri(self.brand_logo.url)


class Query(graphene.ObjectType):
    all_flights = graphene.List(ScheduleType)
    # all_posts = graphene.List(PostType)
    # author_by_username = graphene.Field(AuthorType, username=graphene.String())
    # post_by_slug = graphene.Field(PostType, slug=graphene.String())
    # posts_by_author = graphene.List(PostType, username=graphene.String())
    # posts_by_tag = graphene.List(PostType, tag=graphene.String())

    def resolve_all_flights(root, info):
        return (
            FlightProject.objects.all()
        )
    # def resolve_all_profiles(root, info):
    #     return (
    #         Profile.objects.all()
    #     )

    # def resolve_author_by_username(root, info, username):
    #     return models.Profile.objects.select_related("user").get(
    #         user__username=username
    #     )

    # def resolve_post_by_slug(root, info, slug):
    #     return (
    #         models.AircraftPost.objects.prefetch_related("tags")
    #         .select_related("author")
    #         .get(slug=slug)
    #     )

    # def resolve_posts_by_author(root, info, username):
    #     return (
    #         models.AircraftPost.objects.prefetch_related("tags")
    #         .select_related("author")
    #         .filter(author__user__username=username)
    #     )

    # def resolve_posts_by_tag(root, info, tag):
    #     return (
    #         models.AircraftPost.objects.prefetch_related("tags")
    #         .select_related("author")
    #         .filter(tags__name__iexact=tag)
    #     )

    # def resolve_all_brands(root, info):
    #     return (
    #         models.Manufacturer.objects.all()
    #     )


schema = graphene.Schema(query=Query)
