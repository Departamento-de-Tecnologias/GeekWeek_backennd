from django.db import models

# Create your models here.

class Votation(models.Model):
    """Votation mode"""
    idip = models.GenericIPAddressField(unique=True)
    voteid=models.IntegerField(blank=False)
    