"""GameCategory model module"""
from django.db import models


class GameCategory(models.Model):
    """GameCategory database model"""
    games = models.ForeignKey("Games", on_delete=models.CASCADE, related_name="registrations")
    category = models.ForeignKey("Categores", on_delete=models.CASCADE, related_name="registrations")