from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from fm.models import Motor
from .serializers import MotorSerializer

class MotorAPIView(generics.ListAPIView):
    queryset = Motor.objects.all()
    serializer_class = MotorSerializer