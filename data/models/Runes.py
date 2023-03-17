from django.db import models


class RuneSelection:
    perk = models.IntegerField()
    var3 = models.IntegerField()
    var2 = models.IntegerField()
    var1 = models.IntegerField()
    category = models.ForeignKey("data.RuneCategory", on_delete=models.CASCADE)


RUNE_DESCRIPTIONS = [
    (1, "primaryStyle"),
    (2, "secondaryStyle")
]


class RuneCategory:
    description = models.CharField(choices=RUNE_DESCRIPTIONS)
    style = models.IntegerField()
    participant = models.ForeignKey("data.Participant", on_delete=models.CASCADE)