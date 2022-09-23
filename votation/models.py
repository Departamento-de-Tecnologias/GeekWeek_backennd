from django.db import models

# Create your models here.

class votation(models.Model):
    """Votation mode"""
    idip = models.GenericIPAddressField()
    voteid=models.IntegerField()
    