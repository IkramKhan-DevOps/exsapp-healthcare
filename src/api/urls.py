from django.urls import path, include
from rest_framework import routers

from src.api.views import UserUpdateView, UserImageView, CaloriesConsumptionListView, CaptureListView

app_name = 'api'

urlpatterns = [
    path('capture/', CaptureListView.as_view(), name='capture-list-view'),
    path('calories-consumption/', CaloriesConsumptionListView.as_view(), name='calories-consumption-list-view'),
    path('my/image/', UserImageView.as_view(), name="my-profile"),
    path('my/profile/', UserUpdateView.as_view(), name="my-profile-image"),
]
