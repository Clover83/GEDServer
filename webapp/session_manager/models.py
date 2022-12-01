from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Player(models.Model):
    device_id = models.CharField(max_length=100)
    timestamps = ArrayField(
            models.CharField(max_length=20)
            )
    locations = ArrayField(
            models.CharField(max_length=50)
            )

    def __str__(self):
        return self.device_id

class Session(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=200)
    players= models.ManyToManyField(Player)
   
    def __str__(self):
        return self.name

