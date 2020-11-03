"""Images model module"""
from django.db import models

class Images(models.Model):
    link = models.CharField(max_length=250)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey("Games", on_delete=models.CASCADE)