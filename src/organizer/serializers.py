"""Serializers for the Organizer App

Serializer Documentation
http://www.django-rest-framework.org/api-guide/serializers/
http://www.django-rest-framework.org/api-guide/fields/
http://www.django-rest-framework.org/api-guide/relations/
"""
from rest_framework.reverse import reverse
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedRelatedField,
    ModelSerializer,
    PrimaryKeyRelatedField,
    SerializerMethodField,
    StringRelatedField,
)

from .models import (
    Coach,
    Gym,
    Tag,
    Wod,
)

class TagSerializer(HyperlinkedModelSerializer):
    """Serialize Tag data"""

    class Meta:
        model = Tag
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-tag-detail",
            }
        }

class WodSerializer(HyperlinkedModelSerializer):
    """Serialize Wod data"""
    coach_link = StringRelatedField( many=False, read_only=True, )
    gym_link = StringRelatedField( many=False, read_only=True, )

    tags = HyperlinkedRelatedField(
        lookup_field="slug",
        many=True,
        queryset=Tag.objects.all(),
        view_name="api-tag-detail",
    )

    class Meta:
        model = Wod
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "pk",
                "view_name": "api-wod-detail",
            },
        }

