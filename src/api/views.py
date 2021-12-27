import os

from rest_framework import generics
from rest_framework import permissions

from core import settings
from src.accounts.models import User
from .serializers import (
    CaptureSerializer,
    CaloriesConsumptionSerializer, UserProfileSerializer, UserImageSerializer)

from .models import (
    Capture,
    CaloriesConsumption)


class CaptureListView(generics.ListCreateAPIView):
    queryset = Capture.objects.all()
    serializer_class = CaptureSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        capture = serializer.save(user=self.request.user)

        # AI CALL -------------------------------------
        _file = open(os.path.join(settings.BASE_DIR, 'food_densenet.h5'))
        capture.accuracy = 100
        capture.calories = 100
        capture.category = "No Category"
        capture.save()
        # ---------------------------------------------


class CaloriesConsumptionListView(generics.ListCreateAPIView):
    queryset = CaloriesConsumption.objects.all()
    serializer_class = CaloriesConsumptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserImageView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
