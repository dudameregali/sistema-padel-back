from rest_framework import viewsets
from games.api import serializers
from games import models

class RegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RegistrationSerializer
    queryset = models.Registration.objects.all()

class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SubscriptionSerializer
    queryset = models.Subcription.objects.all()