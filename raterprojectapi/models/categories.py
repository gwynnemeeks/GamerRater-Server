"""Categories model module"""
from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=50)