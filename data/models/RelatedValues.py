from django.db import models


class GameMode(models.Model):
    name = models.CharField(max_length=150)


class Cooldown(models.Model):
    value = models.IntegerField()


class Cost(models.Model):
    value = models.IntegerField()


class Range(models.Model):
    value = models.IntegerField()
