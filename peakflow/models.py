from django.db import models

# Create your models here.


class Reading(models.Model):
    DateTme = models.DateTimeField()
    Reading = models.IntegerField()