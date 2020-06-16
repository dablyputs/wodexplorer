"""URL paths for Organizer App"""
from django.urls import path

from .views import (
    WodCreate,
    WodDelete,
    WodDetail,
    WodList,
    WodUpdate,
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
]
