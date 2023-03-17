from django.db import models
from .abstract.Image import AbstractImage
from .RelatedValues import GameMode
from .Items import Item


class SummonerImage(AbstractImage):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='summoner_image')


class SummonerSpell(models.Model):
    spell_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField()
    tooltip = models.TextField()

    cooldown = models.IntegerField()

    cooldownBurn = models.CharField(max_length=10)
    costBurn = models.CharField(max_length=10)

    key = models.CharField(max_length=10)
    summonerLevel = models.IntegerField()
    costType = models.CharField(max_length=50)

    range = models.OneToOneField(
        "data.Range",
        on_delete=models.CASCADE,
    )

    rangeBurn = models.CharField(max_length=10)
    resource = models.CharField(max_length=50)

    modes = models.ManyToManyField(GameMode)
