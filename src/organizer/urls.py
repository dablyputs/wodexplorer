"""URL paths for Organizer App"""
from django.urls import path

from .views import (
    WodCreate,
    WodDelete,
    WodDetail,
    WodList,
    WodUpdate,
    TagCreate,
    TagDelete,
    TagDetail,
    TagList,
    TagUpdate,
)

urlpatterns = [
    path(
        "wod/",
        WodList.as_view(),
        name="wod_list",
    ),
    path(
        "wod/create/",
        WodCreate.as_view(),
        name="wod_create",
    ),
    path(
        "wod/<str:pk>/",
        WodDetail.as_view(),
        name="wod_detail",
    ),
    path(
        "wod/<str:pk>/delete/",
        WodDelete.as_view(),
        name="wod_delete",
    ),
    path(
        "wod/<str:pk>/update/",
        WodUpdate.as_view(),
        name="wod_update",
    ),
    path("tag/", TagList.as_view(), name="tag_list"),
    path(
        "tag/create/",
        TagCreate.as_view(),
        name="tag_create",
    ),
    path(
        "tag/<str:slug>/",
        TagDetail.as_view(),
        name="tag_detail",
    ),
    path(
        "tag/<str:slug>/update/",
        TagUpdate.as_view(),
        name="tag_update",
    ),
    path(
        "tag/<str:slug>/delete/",
        TagDelete.as_view(),
        name="tag_delete",
    ),
]
