from django.db import models


class AbstractImage(models.Model):
    full = models.CharField(max_length=100)
    sprite = models.CharField(max_length=100)
    group = models.CharField(max_length=50)
    x = models.IntegerField()
    y = models.IntegerField()
    w = models.IntegerField()
    h = models.IntegerField()

    class Meta:
        abstract = True
