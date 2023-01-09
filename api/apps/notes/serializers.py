from django.urls import path, include
from apps.users.models import User
from apps.notes.models import Note, NoteShares, Collection
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.

class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collection
        fields = ['get_bookmark_url',]

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.StringRelatedField(many=False)
    obj = serializers.StringRelatedField(many=False)
    class Meta:
        model = Note
        fields = ['id', 'obj', 'author', 'title', 'content', 'createAt', 'updateAt', ]


class NoteSharesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NoteShares
        fields = ['id', 'owner', 'title', 'shared_with', 'parent',]\

