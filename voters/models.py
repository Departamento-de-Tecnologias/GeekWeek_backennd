from django.db import models

# Create your models here.

class Voters(models.Model):
    """Voters Models"""
    id = models.AutoField(primary_key=True)
    url = models.URLField(blank=False)
    votes = models.IntegerField(default=0)