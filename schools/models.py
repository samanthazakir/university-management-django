from django.db import models


class School(models.Model):
    name     = models.CharField(max_length=255)
    headName = models.CharField(max_length=255)
    location = models.CharField(max_length=511)
