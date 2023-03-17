from django.db import models


OBJECTIVE_CHOICES = [
    ('BARON', 'Baron'),
    ('CHAMP', 'Champion'),
    ('DRAKE', 'Dragon'),
    ('INHIB', 'Inhibitor'),
    ('RIFT', 'Rift Herald'),
    ("TOWER", "Tower")
]


class Objective(models.Model):
    choices = [
        'BARON',
        'CHAMP',
        'DRAKE',
        'INHIB',
        'RIFT',
        "TOWER",
    ]
    name = models.CharField(max_length=10, choices=OBJECTIVE_CHOICES)
    first = models.BooleanField()
    kills = models.IntegerField()
    team = models.ForeignKey("data.Team", on_delete=models.CASCADE)


class Ban(models.Model):
    champion_id = models.IntegerField()
    pick_turn = models.IntegerField()
    team = models.ForeignKey("data.Team", on_delete=models.CASCADE)


class Team(models.Model):
    team_id = models.IntegerField()
    win = models.BooleanField()
    match = models.ForeignKey("data.Match", on_delete=models.CASCADE)