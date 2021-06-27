from django.db import models

# Create your models here.

class roomcodes(models.Model) :
    roomcode = models.CharField(max_length=8)

class users(models.Model) :
    name = models.CharField(max_length=10)
    roomcode = models.CharField(max_length=8)

class day_profit(models.Model) :
    team1 = models.FloatField()
    team2 = models.FloatField()
    team3 = models.FloatField()
    team4 = models.FloatField()
    roomcode = models.CharField(max_length=8)
    day = models.IntegerField(max_length=1)