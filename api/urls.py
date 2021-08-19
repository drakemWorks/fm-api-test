# api/urls.py
from django.urls import path
from .views import MotorAPIView

urlpatterns = [
    path('', MotorAPIView.as_view()),
]