from django.db import models
from . import Participant

RUNE_DESCRIPTIONS = [
    ("1", "primaryStyle"),
    ("2", "secondaryStyle")
]


class RuneCategory(models.Model):
    description = models.CharField(choices=RUNE_DESCRIPTIONS, max_length=50)
    style = models.IntegerField()
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)


class RuneSelection(models.Model):
    perk = models.IntegerField()
    var3 = models.IntegerField()
    var2 = models.IntegerField()
    var1 = models.IntegerField()
    category = models.ForeignKey(RuneCategory, on_delete=models.CASCADE)


class StatPerks(models.Model):
    defense = models.IntegerField()
    flex = models.IntegerField()
    offense = models.IntegerField()
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
