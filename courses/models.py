from django.db import models

from schools.models import School

class Course(models.Model):
    name = models.CharField(max_length=255)
    coordinator = models.CharField(max_length=255)
    total_credits = models.DecimalField(max_digits=6, decimal_places=3)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='courses')
