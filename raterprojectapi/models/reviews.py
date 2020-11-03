"""Reviews model module"""
from django.db import models

class Reviews(models.Model):
    review_body = models.CharField(max_length=50)
    timestamp = models.TimeField(auto_now=False, auto_now_add=False)
    rating = models.IntegerField()
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey("Games", on_delete=models.CASCADE)