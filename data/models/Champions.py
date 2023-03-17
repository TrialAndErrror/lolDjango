from django.db import models
from .abstract.Image import AbstractImage


class ChampionTag(models.Model):
    name = models.CharField(max_length=50)


class Champion(models.Model):
    version = models.CharField(max_length=10)
    champion_id = models.CharField(max_length=50)
    key = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    blurb = models.TextField()
    par_type = models.CharField(max_length=50)

    tags = models.ManyToManyField(ChampionTag)


class ChampionImage(AbstractImage):
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE, related_name='image')


class ChampionInfo(models.Model):
    attack = models.IntegerField()
    defense = models.IntegerField()
    magic = models.IntegerField()
    difficulty = models.IntegerField()
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE, related_name='info')


class ChampionStats(models.Model):
    hp = models.IntegerField()
    hp_per_level = models.IntegerField()
    mp = models.IntegerField()
    mp_per_level = models.IntegerField()
    move_speed = models.IntegerField()
    armor = models.FloatField()
    armor_per_level = models.FloatField()
    spell_block = models.FloatField()
    spell_block_per_level = models.FloatField()
    attack_range = models.IntegerField()
    hp_regen = models.FloatField()
    hp_regen_per_level = models.FloatField()
    mp_regen = models.FloatField()
    mp_regen_per_level = models.FloatField()
    crit = models.FloatField()
    crit_per_level = models.FloatField()
    attack_damage = models.FloatField()
    attack_damage_per_level = models.FloatField()
    attack_speed_per_level = models.FloatField()
    attack_speed = models.FloatField()
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE, related_name='stats')
