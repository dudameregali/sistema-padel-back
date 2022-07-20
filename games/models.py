from tkinter import CASCADE
from uuid import uuid4
from django.db import models
from cpf_field.models import CPFField

# Create your models here.

from django.db import models

# Create your models here.

class Registration(models.Model):
    cpf = CPFField('cpf', primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    city = models.CharField(max_length=255)
    points = models.FloatField()

class Subcription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    playerOne = models.ForeignKey('Registration', on_delete=models.CASCADE, related_name='playerOne')
    playerTwo = models.ForeignKey('Registration', on_delete=models.CASCADE, related_name='playerTwo')
    category = models.CharField(max_length=255)
    pairPoint = models.FloatField()