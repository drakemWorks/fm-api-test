from django.shortcuts import render
from django.views.generic import ListView
from .models import Motor

# Create your views here.
class MotorListView(ListView):
    model = Motor
    template_name = "motor_list.html"
