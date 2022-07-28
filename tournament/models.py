from django.db import models
from games.api.serializers import SubscriptionSerializer
from games.models import Subcription as subscription

# Create your models here.

class Tournament(models.Model):
    numberOfSubscribers = models.IntegerField()
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    numberOfCourts = models.IntegerField()

    def assemblyOfGroups(category):
        filtro = subscription.objects.filter(subscription.category == category).order_by(subscription.pairPoint)
        numberOfPair = filtro.count()

        groupOne = []
        groupTwo = []

        for i in range(1, numberOfPair):
            filter.