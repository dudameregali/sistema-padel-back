from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from games import models

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Registration
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subcription
        fields = '__all__'

