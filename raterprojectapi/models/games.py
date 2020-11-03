"""Games model module"""
from django.db import models

class Games(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    designer = models.CharField(max_length=50)
    year_released = models.IntegerField()
    num_of_players = models.IntegerField()
    play_time = models.CharField(max_length=50)
    ages = models.CharField(max_length=50)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)