from rest_framework import serializers
from fm.models import Motor


class MotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motor
        fields = ('oem','qty','hp')