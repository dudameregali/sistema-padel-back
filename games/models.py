from tkinter import CASCADE
from uuid import uuid4
from django.db import models
from cpf_field.models import CPFField

# Create your models here.

choicesOfCategory = (
        ('FIni','Feminino Iniciante'),
        ('FInt', 'Feminino Intermediário'),
        ('FAva', 'Feminino Avançado'),
        ('MIni', 'Masculino Iniciante'),
        ('MInt', 'Masculino Intermediário'),
        ('MAva', 'Masculino Avançado'),
    )

class Registration(models.Model):
    cpf = CPFField('cpf', primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    city = models.CharField(max_length=255)
    points = models.FloatField()

class Subcription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    playerOne = models.ForeignKey('Registration', on_delete=models.CASCADE, related_name='playerOne')
    playerTwo = models.ForeignKey('Registration', on_delete=models.CASCADE, related_name='playerTwo')
    category = models.CharField(max_length=4, choices=choicesOfCategory)
    pairPoint = models.FloatField()
    #teste = Registration.objects.filter(Registration.cpf == playerOne or Registration.cpf == playerTwo)

