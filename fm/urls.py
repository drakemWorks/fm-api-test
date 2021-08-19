from django.urls import path
from .views import MotorListView

urlpatterns = [
    path('', MotorListView.as_view(), name='home'),
]
